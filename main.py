from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import random
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Load AI Model for NLP-based grading
nlp_model = pipeline("text-generation", model="facebook/bart-large-cnn")

# Connect to MongoDB (Store feedback & student data)
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client["teacher_assistant"]
grades_collection = db["grades"]

# Define request model
class AnswerSubmission(BaseModel):
    student_id: str
    question_type: str  # "mcq" or "subjective"
    question: str
    answer: str
    correct_answer: str = None  # For MCQs

# Function to grade MCQs
def grade_mcq(answer, correct_answer):
    return 1 if answer.strip().lower() == correct_answer.strip().lower() else 0

# Function to grade subjective answers (NLP)
def grade_subjective(answer):
    feedback = nlp_model(answer, max_length=50, num_return_sequences=1)[0]['generated_text']
    score = random.randint(5, 10)  # Placeholder for real AI evaluation
    return score, feedback

# API endpoint for grading
@app.post("/grade")
def grade_answer(submission: AnswerSubmission):
    if submission.question_type == "mcq":
        score = grade_mcq(submission.answer, submission.correct_answer)
        feedback = "Correct answer!" if score == 1 else "Incorrect, review this topic."
    else:
        score, feedback = grade_subjective(submission.answer)

    # Store result in DB
    grades_collection.insert_one({
        "student_id": submission.student_id,
        "question": submission.question,
        "answer": submission.answer,
        "score": score,
        "feedback": feedback
    })

    return {"student_id": submission.student_id, "score": score, "feedback": feedback}
