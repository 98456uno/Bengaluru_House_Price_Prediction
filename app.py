# # # # # # # # # app.py

# # # # # # # # import streamlit as st
# # # # # # # # import pickle
# # # # # # # # import numpy as np
# # # # # # # # import base64


# # # # # # # # # Set background
# # # # # # # # def set_bg(jpg_file):
# # # # # # # #     with open(jpg_file, "rb") as file:
# # # # # # # #         b64_img = base64.b64encode(file.read()).decode()
# # # # # # # #     st.markdown(
# # # # # # # #         f"""
# # # # # # # #         <style>
# # # # # # # #         .stApp {{
# # # # # # # #             background-image: url("data:image/jpg;base64,{b64_img}");
# # # # # # # #             background-size: cover;
# # # # # # # #             background-attachment: fixed;
# # # # # # # #             background-repeat: no-repeat;
# # # # # # # #         }}
# # # # # # # #         </style>
# # # # # # # #         """,
# # # # # # # #         unsafe_allow_html=True
# # # # # # # #     )

# # # # # # # # set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\ai-generated-real-estate-advertisment-background-with-copy-space-free-photo.jpg")

# # # # # # # # # Load model and columns
# # # # # # # # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # # # # # # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']

# # # # # # # # locations = data_columns[3:]

# # # # # # # # # App Title
# # # # # # # # st.markdown("<h1 style='text-align: center; color: #2d3436;'>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)
# # # # # # # # st.markdown("---")

# # # # # # # # # Inputs
# # # # # # # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")
# # # # # # # # bhk = st.radio("Select BHK:", [1, 2, 3, 4, "5+"])
# # # # # # # # bath = st.radio("Select Bathrooms:", [1, 2, 3, 4, "5+"])
# # # # # # # # location = st.selectbox("Select Location:", sorted(locations))

# # # # # # # # bhk = 5 if bhk == "5+" else bhk
# # # # # # # # bath = 5 if bath == "5+" else bath

# # # # # # # # # Predict Button
# # # # # # # # if st.button("Estimate Price 💰"):
# # # # # # # #     try:
# # # # # # # #         input_vector = np.zeros(len(data_columns))
# # # # # # # #         input_vector[0] = float(sqft)
# # # # # # # #         input_vector[1] = bath
# # # # # # # #         input_vector[2] = bhk
# # # # # # # #         if location in data_columns:
# # # # # # # #             loc_index = data_columns.index(location)
# # # # # # # #             input_vector[loc_index] = 1

# # # # # # # #         predicted_price = model.predict([input_vector])[0]
# # # # # # # #         st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")

# # # # # # # #     except:
# # # # # # # #         st.error("Please enter a valid numeric area.")
# # # # # # # # Add this at the top with other imports
# # # # # # # import streamlit as st
# # # # # # # import pickle
# # # # # # # import numpy as np
# # # # # # # import base64

# # # # # # # # Background image setup
# # # # # # # def set_bg(png_file):
# # # # # # #     with open(png_file, "rb") as f:
# # # # # # #         b64_img = base64.b64encode(f.read()).decode()
# # # # # # #     st.markdown(
# # # # # # #         f"""
# # # # # # #         <style>
# # # # # # #         .stApp {{
# # # # # # #             background-image: url("data:image/jpg;base64,{b64_img}");
# # # # # # #             background-size: cover;
# # # # # # #             background-repeat: no-repeat;
# # # # # # #             background-attachment: fixed;
# # # # # # #         }}

# # # # # # #         .form-box {{
# # # # # # #             background-color: rgba(0, 0, 0, 0.6);  /* semi-transparent black */
# # # # # # #             padding: 2rem;
# # # # # # #             border-radius: 15px;
# # # # # # #             max-width: 600px;
# # # # # # #             margin: auto;
# # # # # # #         }}

# # # # # # #         .form-box h1 {{
# # # # # # #             color: #ffffff;
# # # # # # #             text-align: center;
# # # # # # #         }}

# # # # # # #         label, .stTextInput, .stRadio, .stSelectbox, .stButton {{
# # # # # # #             color: #ffffff !important;
# # # # # # #         }}
# # # # # # #         </style>
# # # # # # #         """,
# # # # # # #         unsafe_allow_html=True
# # # # # # #     )

# # # # # # # set_bg(r"ai-generated-real-estate-advertisment-background-with-copy-space-free-photo.jpg")  # background

# # # # # # # # Load model and data columns
# # # # # # # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # # # # # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']
# # # # # # # locations = data_columns[3:]

# # # # # # # # Start UI
# # # # # # # st.markdown('<div class="form-box">', unsafe_allow_html=True)
# # # # # # # st.markdown("<h1>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)

# # # # # # # # Form
# # # # # # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")
# # # # # # # # Replace st.radio with st.select_slider

# # # # # # # bhk = st.select_slider("Select BHK:", options=[1, 2, 3, 4, 5], value=2)
# # # # # # # bath = st.select_slider("Select Bathrooms:", options=[1, 2, 3, 4, 5], value=2)

# # # # # # # location = st.selectbox("Select Location:", sorted(locations))

# # # # # # # # Normalize input
# # # # # # # bhk = 5 if bhk == "5+" else bhk
# # # # # # # bath = 5 if bath == "5+" else bath

# # # # # # # # Prediction
# # # # # # # if st.button("Estimate Price 💰"):
# # # # # # #     try:
# # # # # # #         input_vector = np.zeros(len(data_columns))
# # # # # # #         input_vector[0] = float(sqft)
# # # # # # #         input_vector[1] = bath
# # # # # # #         input_vector[2] = bhk
# # # # # # #         if location in data_columns:
# # # # # # #             loc_index = data_columns.index(location)
# # # # # # #             input_vector[loc_index] = 1
# # # # # # #         predicted_price = model.predict([input_vector])[0]
# # # # # # #         st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
# # # # # # #     except:
# # # # # # #         st.error("❌ Please enter a valid numeric area.")

# # # # # # # st.markdown("</div>", unsafe_allow_html=True)
# # # # # # import streamlit as st
# # # # # # import pickle
# # # # # # import numpy as np
# # # # # # import base64

# # # # # # # Load background
# # # # # # def set_bg(png_file):
# # # # # #     with open(png_file, "rb") as f:
# # # # # #         b64_img = base64.b64encode(f.read()).decode()
# # # # # #     st.markdown(
# # # # # #         f"""
# # # # # #         <style>
# # # # # #         .stApp {{
# # # # # #             background-image: url("data:image/jpg;base64,{b64_img}");
# # # # # #             background-size: cover;
# # # # # #             background-repeat: no-repeat;
# # # # # #             background-attachment: fixed;
# # # # # #         }}

# # # # # #         .form-box {{
# # # # # #             background-color: rgba(0, 0, 0, 0.6);
# # # # # #             padding: 2rem;
# # # # # #             border-radius: 15px;
# # # # # #             max-width: 600px;
# # # # # #             margin: 3rem auto;
# # # # # #             color: white;
# # # # # #         }}

# # # # # #         .form-box h1 {{
# # # # # #             color: #ffffff;
# # # # # #             text-align: center;
# # # # # #         }}
# # # # # #         </style>
# # # # # #         """,
# # # # # #         unsafe_allow_html=True
# # # # # #     )

# # # # # # set_bg("WhatsApp Image 2025-07-03 at 21.45.16_80d693e7.jpg")

# # # # # # # Load model and columns
# # # # # # model = pickle.load(open("banglore_home_prices_model.pickle", "rb"))
# # # # # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']
# # # # # # locations = data_columns[3:]  # skip sqft, bath, bhk

# # # # # # def is_float(val):
# # # # # #     try:
# # # # # #         float(val)
# # # # # #         return True
# # # # # #     except:
# # # # # #         return False

# # # # # # # UI
# # # # # # st.markdown('<div class="form-box">', unsafe_allow_html=True)
# # # # # # st.markdown("<h1>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)

# # # # # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")

# # # # # # bhk = st.select_slider("Select BHK:", options=[1, 2, 3, 4, 5], value=2)
# # # # # # bath = st.select_slider("Select Bathrooms:", options=[1, 2, 3, 4, 5], value=2)

# # # # # # location = st.selectbox("Select Location:", sorted(locations))

# # # # # # # Prediction
# # # # # # if st.button("Estimate Price 💰"):
# # # # # #     if is_float(sqft):
# # # # # #         try:
# # # # # #             sqft = float(sqft)
# # # # # #             input_vector = np.zeros(len(data_columns))
# # # # # #             input_vector[0] = sqft
# # # # # #             input_vector[1] = bath
# # # # # #             input_vector[2] = bhk
# # # # # #             if location in data_columns:
# # # # # #                 loc_index = data_columns.index(location)
# # # # # #                 input_vector[loc_index] = 1
# # # # # #             predicted_price = model.predict([input_vector])[0]
# # # # # #             st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
# # # # # #         except Exception as e:
# # # # # #             st.error(f"❌ Prediction failed: {e}")
# # # # # #     else:
# # # # # #         st.error("❌ Please enter a valid numeric area.")

# # # # # # st.markdown('</div>', unsafe_allow_html=True)

# # # # # import streamlit as st
# # # # # import pickle
# # # # # import numpy as np
# # # # # import base64

# # # # # # -------------------- Set Background Image --------------------
# # # # # def set_bg(jpg_file):
# # # # #     with open(jpg_file, "rb") as f:
# # # # #         b64_img = base64.b64encode(f.read()).decode()
# # # # #     st.markdown(
# # # # #         # inside set_bg function
# # # # # f"""
# # # # # <style>
# # # # # .stApp {{
# # # # #     background-image: url("data:image/jpg;base64,{b64_img}");
# # # # #     background-size: cover;
# # # # #     background-repeat: no-repeat;
# # # # #     background-attachment: fixed;
# # # # # }}

# # # # # .form-box {{
# # # # #     background-color: rgba(255, 255, 255, 0.92); /* white, semi-transparent */
# # # # #     padding: 2rem 2rem 2.5rem 2rem;
# # # # #     border-radius: 20px;
# # # # #     max-width: 450px;   /* 💡 Narrower width */
# # # # #     margin: 4rem auto;
# # # # #     box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
# # # # # }}

# # # # # .form-box h1 {{
# # # # #     color: #222;
# # # # #     text-align: center;
# # # # #     font-size: 1.8rem;
# # # # #     margin-bottom: 1.5rem;
# # # # # }}

# # # # # label, .stTextInput label, .stSelectbox label, .stSlider label {{
# # # # #     color: #111 !important;
# # # # #     font-weight: 500;
# # # # # }}

# # # # # .stButton>button {{
# # # # #     background-color: #f9c74f;
# # # # #     color: black;
# # # # #     font-weight: bold;
# # # # #     border-radius: 10px;
# # # # #     width: 100%;
# # # # #     height: 3rem;
# # # # #     font-size: 1rem;
# # # # # }}

# # # # # .stButton>button:hover {{
# # # # #     background-color: #f9844a;
# # # # #     color: white;
# # # # # }}
# # # # # </style>
# # # # # """,

# # # # #         unsafe_allow_html=True
# # # # #     )

# # # # # # Apply background
# # # # # set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\ai-generated-real-estate-advertisment-background-with-copy-space-free-photo.jpg")

# # # # # # -------------------- Load Model & Columns --------------------
# # # # # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # # # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']
# # # # # locations = data_columns[3:]

# # # # # def is_float(val):
# # # # #     try:
# # # # #         float(val)
# # # # #         return True
# # # # #     except:
# # # # #         return False

# # # # # # -------------------- UI Layout --------------------
# # # # # st.markdown('<div class="form-box">', unsafe_allow_html=True)
# # # # # st.markdown("<h1>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)

# # # # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")

# # # # # bhk = st.select_slider("Select BHK:", options=[1, 2, 3, 4, 5], value=3)
# # # # # bath = st.select_slider("Select Bathrooms:", options=[1, 2, 3, 4, 5], value=2)

# # # # # location = st.selectbox("Select Location:", sorted(locations))

# # # # # # -------------------- Prediction Logic --------------------
# # # # # if st.button("Estimate Price 💰"):
# # # # #     if is_float(sqft):
# # # # #         try:
# # # # #             input_vector = np.zeros(len(data_columns))
# # # # #             input_vector[0] = float(sqft)
# # # # #             input_vector[1] = bath
# # # # #             input_vector[2] = bhk
# # # # #             if location in data_columns:
# # # # #                 loc_index = data_columns.index(location)
# # # # #                 input_vector[loc_index] = 1
# # # # #             predicted_price = model.predict([input_vector])[0]
# # # # #             st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
# # # # #         except Exception as e:
# # # # #             st.error(f"❌ Prediction failed: {e}")
# # # # #     else:
# # # # #         st.error("❌ Please enter a valid numeric area (e.g. 1200).")

# # # # # st.markdown('</div>', unsafe_allow_html=True)



# # # # import streamlit as st
# # # # import pickle
# # # # import numpy as np
# # # # import base64

# # # # # -------------------- Set Background Image --------------------
# # # # def set_bg(jpg_file):
# # # #     with open(jpg_file, "rb") as f:
# # # #         b64_img = base64.b64encode(f.read()).decode()
# # # #     st.markdown(
# # # #         f"""
# # # #         <style>
# # # #         .stApp {{
# # # #             background-image: url("data:image/jpg;base64,{b64_img}");
# # # #             background-size: cover;
# # # #             background-repeat: no-repeat;
# # # #             background-attachment: fixed;
# # # #         }}

# # # #         .main-box {{
# # # #             background-color: rgba(255, 255, 255, 0.92);
# # # #             padding: 3rem 2.5rem;
# # # #             border-radius: 25px;
# # # #             max-width: 700px;
# # # #             margin: 3rem auto;
# # # #             box-shadow: 0 0 25px rgba(0, 0, 0, 0.25);
# # # #         }}

# # # #         .main-box h1 {{
# # # #             color: #222;
# # # #             text-align: center;
# # # #             font-size: 2rem;
# # # #             margin-bottom: 2rem;
# # # #         }}

# # # #         label, .stTextInput label, .stSelectbox label, .stSlider label {{
# # # #             color: #111 !important;
# # # #             font-weight: 500;
# # # #         }}

# # # #         .stButton>button {{
# # # #             background-color: #f9c74f;
# # # #             color: black;
# # # #             font-weight: bold;
# # # #             border-radius: 10px;
# # # #             width: 100%;
# # # #             height: 3rem;
# # # #             font-size: 1rem;
# # # #         }}

# # # #         .stButton>button:hover {{
# # # #             background-color: #f9844a;
# # # #             color: white;
# # # #         }}
# # # #         </style>
# # # #         """,
# # # #         unsafe_allow_html=True
# # # #     )

# # # # # Apply background
# # # # set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\ai-generated-real-estate-advertisment-background-with-copy-space-free-photo.jpg")

# # # # # -------------------- Load Model & Columns --------------------
# # # # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']
# # # # locations = data_columns[3:]

# # # # def is_float(val):
# # # #     try:
# # # #         float(val)
# # # #         return True
# # # #     except:
# # # #         return False

# # # # # -------------------- Main UI Block --------------------
# # # # st.markdown('<div class="main-box">', unsafe_allow_html=True)
# # # # st.markdown("<h1>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)

# # # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")
# # # # bhk = st.select_slider("Select BHK:", options=[1, 2, 3, 4, 5], value=3)
# # # # bath = st.select_slider("Select Bathrooms:", options=[1, 2, 3, 4, 5], value=2)
# # # # location = st.selectbox("Select Location:", sorted(locations))

# # # # # -------------------- Prediction Logic --------------------
# # # # if st.button("Estimate Price 💰"):
# # # #     if is_float(sqft):
# # # #         try:
# # # #             input_vector = np.zeros(len(data_columns))
# # # #             input_vector[0] = float(sqft)
# # # #             input_vector[1] = bath
# # # #             input_vector[2] = bhk
# # # #             if location in data_columns:
# # # #                 loc_index = data_columns.index(location)
# # # #                 input_vector[loc_index] = 1
# # # #             predicted_price = model.predict([input_vector])[0]
# # # #             st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
# # # #         except Exception as e:
# # # #             st.error(f"❌ Prediction failed: {e}")
# # # #     else:
# # # #         st.error("❌ Please enter a valid numeric area (e.g. 1200).")

# # # # st.markdown('</div>', unsafe_allow_html=True)


# # # import streamlit as st
# # # import pickle
# # # import numpy as np
# # # import base64

# # # # -------------------- Set Background Image --------------------
# # # def set_bg(jpg_file):
# # #     with open(jpg_file, "rb") as f:
# # #         b64_img = base64.b64encode(f.read()).decode()
# # #     st.markdown(
# # #         f"""
# # #         <style>
# # #         .stApp {{
# # #             background-image: url("data:image/jpg;base64,{b64_img}");
# # #             background-size: cover;
# # #             background-repeat: no-repeat;
# # #             background-attachment: fixed;
# # #         }}

# # #         .main-box {{
# # #             background-color: rgba(255, 255, 255, 0.92);
# # #             padding: 3rem 2.5rem;
# # #             border-radius: 25px;
# # #             max-width: 600px;
# # #             margin: 4rem auto;
# # #             box-shadow: 0 0 25px rgba(0, 0, 0, 0.25);
# # #         }}

# # #         .main-box h1 {{
# # #             color: #222;
# # #             text-align: center;
# # #             font-size: 2rem;
# # #             margin-bottom: 2rem;
# # #         }}

# # #         label, .stTextInput label, .stSelectbox label, .stSlider label {{
# # #             color: #111 !important;
# # #             font-weight: 500;
# # #         }}

# # #         .stButton>button {{
# # #             background-color: #f9c74f;
# # #             color: black;
# # #             font-weight: bold;
# # #             border-radius: 10px;
# # #             width: 100%;
# # #             height: 3rem;
# # #             font-size: 1rem;
# # #         }}

# # #         .stButton>button:hover {{
# # #             background-color: #f9844a;
# # #             color: white;
# # #         }}
# # #         </style>
# # #         """,
# # #         unsafe_allow_html=True
# # #     )

# # # # -------------------- Set Background --------------------
# # # set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\ai-generated-real-estate-advertisment-background-with-copy-space-free-photo.jpg")

# # # # -------------------- Load Model & Data --------------------
# # # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # # data_columns = pickle.load(open("columns.pkl", "rb"))['data_columns']
# # # locations = data_columns[3:]

# # # def is_float(val):
# # #     try:
# # #         float(val)
# # #         return True
# # #     except:
# # #         return False

# # # # -------------------- Main Container Start --------------------
# # # st.markdown('<div class="main-box">', unsafe_allow_html=True)

# # # # 🏠 Title
# # # st.markdown("<h1>🏠 Bangalore Home Price Predictor</h1>", unsafe_allow_html=True)

# # # # 📥 Inputs
# # # sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")
# # # bhk = st.select_slider("Select BHK:", options=[1, 2, 3, 4, 5], value=3)
# # # bath = st.select_slider("Select Bathrooms:", options=[1, 2, 3, 4, 5], value=2)
# # # location = st.selectbox("Select Location:", sorted(locations))

# # # # 🔮 Prediction Button
# # # if st.button("Estimate Price 💰"):
# # #     if is_float(sqft):
# # #         try:
# # #             input_vector = np.zeros(len(data_columns))
# # #             input_vector[0] = float(sqft)
# # #             input_vector[1] = bath
# # #             input_vector[2] = bhk
# # #             if location in data_columns:
# # #                 loc_index = data_columns.index(location)
# # #                 input_vector[loc_index] = 1
# # #             predicted_price = model.predict([input_vector])[0]
# # #             st.success(f"🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs")
# # #         except Exception as e:
# # #             st.error(f"❌ Prediction failed: {e}")
# # #     else:
# # #         st.error("❌ Please enter a valid numeric area (e.g. 1200).")

# # # # -------------------- Main Container End --------------------
# # # st.markdown('</div>', unsafe_allow_html=True)
 

# # import streamlit as st
# # import pickle
# # import numpy as np
# # import base64
# # import json

# # # -------------------- Set Background Image --------------------
# # def set_bg(jpg_file):
# #     with open(jpg_file, "rb") as f:
# #         b64_img = base64.b64encode(f.read()).decode()
# #     st.markdown(
# #         f"""
# #         <style>
# #         .stApp {{
# #             background-image: url("data:image/jpg;base64,{b64_img}");
# #             background-size: cover;
# #             background-repeat: no-repeat;
# #             background-attachment: fixed;
# #         }}

        
      


# #         label, .stTextInput label, .stSelectbox label, .stSlider label {{
# #             color: #111 !important;
# #             font-weight: 500;
# #         }}

# #         .stButton>button {{
# #             background-color: #f9c74f;
# #             color: black;
# #             font-weight: bold;
# #             border-radius: 10px;
# #             width: 100%;
# #             height: 3rem;
# #             font-size: 1rem;
# #         }}

# #         .stButton>button:hover {{
# #             background-color: #f9844a;
# #             color: white;
# #         }}


        
# # /* Make radio buttons look like square buttons */
# # div[data-baseweb="radio"] > div {
# #     flex-wrap: nowrap;
# #     gap: 10px;
# # }

# # div[data-baseweb="radio"] label {
# #     background-color: #f0f0f0;
# #     padding: 12px 18px;
# #     border-radius: 8px;
# #     border: 2px solid #ccc;
# #     color: black;
# #     font-weight: bold;
# #     cursor: pointer;
# #     transition: all 0.3s ease;
# # }

# # div[data-baseweb="radio"] label:hover {
# #     background-color: #f9c74f;
# #     border-color: #f9844a;
# #     color: black;
# # }

# # div[data-baseweb="radio"] input:checked + div {
# #     background-color: #f9844a !important;
# #     border-color: #f3722c !important;
# #     color: white !important;
# # }

# # /* Hide default circle */
# # div[data-baseweb="radio"] svg {
# #     display: none;
# # }
# # </style>

    
# #         """,
# #         unsafe_allow_html=True
# #     )

# # # -------------------- Set Background --------------------
# # set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\Untitled design.jpg")

# # # -------------------- Load Model & Columns --------------------
# # model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# # data_columns = json.load(open("columns.json", "rb"))['data_columns']
# # locations = data_columns[3:]

# # def is_float(val):
# #     try:
# #         float(val)
# #         return True
# #     except:
# #         return False

# # # -------------------- Render Main Box --------------------
# # with st.container():
# #     st.markdown('<div class="main-box">', unsafe_allow_html=True)

# #     st.markdown('<h1 style="color: black;">🏠 Bangalore Home Price Predictor</h1>', unsafe_allow_html=True)


# #     sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")
# #     bhk = st.radio("Select BHK:", options=[1, 2, 3, 4, 5], horizontal=True)
# #     bath = st.radio("Select Bathrooms:", options=[1, 2, 3, 4, 5], horizontal=True)


# #     location = st.selectbox("Select Location:", sorted(locations))

# #     if st.button("Estimate Price 💰"):
# #         if is_float(sqft):
# #             try:
# #                 input_vector = np.zeros(len(data_columns))
# #                 input_vector[0] = float(sqft)
# #                 input_vector[1] = bath
# #                 input_vector[2] = bhk
# #                 if location in data_columns:
# #                     loc_index = data_columns.index(location)
# #                     input_vector[loc_index] = 1
# #                 predicted_price = model.predict([input_vector])[0]
# #                 st.markdown(
# #     f"""
# #     <div style='background-color: #d4edda; padding: 12px 20px; border-radius: 10px;
# #                 color: black; font-weight: bold; font-size: 18px;
# #                 border-left: 6px solid #28a745; margin-top: 20px;'>
# #         🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

# #             except Exception as e:
# #                 st.markdown(
# #     f"""
# #     <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
# #                 color: black; font-weight: bold; font-size: 16px;
# #                 border-left: 6px solid #dc3545; margin-top: 20px;'>
# #         ❌ Prediction failed: {e}
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )
# #         else:
# #            st.markdown(
# #     """
# #     <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
# #                 color: black; font-weight: bold; font-size: 16px;
# #                 border-left: 6px solid #dc3545; margin-top: 20px;'>
# #         ❌ Please enter a valid numeric area (e.g. 1200).
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

# # st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# import pickle
# import numpy as np
# import base64
# import json

# # -------------------- Set Background Image --------------------
# def set_bg(jpg_file):
#     with open(jpg_file, "rb") as f:
#         b64_img = base64.b64encode(f.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{b64_img}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}

       

#         .main-box h1 {{
#             color: #222;
#             text-align: center;
#             font-size: 2rem;
#             margin-bottom: 2rem;
#         }}

#         label, .stTextInput label, .stSelectbox label {{
#             color: #111 !important;
#             font-weight: 500;
#         }}

#         .stButton>button {{
#             background-color: #f9c74f;
#             color: black;
#             font-weight: bold;
#             border-radius: 10px;
#             width: 100%;
#             height: 3rem;
#             font-size: 1rem;
#         }}

#         .stButton>button:hover {{
#             background-color: #f9844a;
#             color: white;
#         }}

#         /* Custom styled radio buttons as square buttons */
#         div[data-baseweb="radio"] > div {{
#             flex-wrap: nowrap;
#             gap: 10px;
#         }}

#         div[data-baseweb="radio"] label {{
#             background-color: #f0f0f0;
#             padding: 12px 18px;
#             border-radius: 8px;
#             border: 2px solid #ccc;
#             color: black;
#             font-weight: bold;
#             cursor: pointer;
#             transition: all 0.3s ease;
#         }}

#         div[data-baseweb="radio"] label:hover {{
#             background-color: #f9c74f;
#             border-color: #f9844a;
#             color: black;
#         }}

#         div[data-baseweb="radio"] input:checked + div {{
#             background-color: #f9844a !important;
#             border-color: #f3722c !important;
#             color: white !important;
#         }}

#         div[data-baseweb="radio"] svg {{
#             display: none;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------- Set Background --------------------
# set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\Untitled design.jpg")

# # -------------------- Load Model & Data Columns --------------------
# model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# data_columns = json.load(open("columns.json", "rb"))['data_columns']
# locations = data_columns[3:]

# # -------------------- Helper Function --------------------
# def is_float(val):
#     try:
#         float(val)
#         return True
#     except:
#         return False

# # -------------------- Main UI --------------------
# with st.container():
#     st.markdown('<div class="main-box">', unsafe_allow_html=True)
#     st.markdown('<h1 style="color: black;">🏠 Bangalore Home Price Predictor</h1>', unsafe_allow_html=True)

#     sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")

#     bhk = st.radio("Select BHK:", options=[1, 2, 3, 4, 5], horizontal=True)
#     bath = st.radio("Select Bathrooms:", options=[1, 2, 3, 4, 5], horizontal=True)

#     location = st.selectbox("Select Location:", sorted(locations))

#     # -------------------- Prediction Logic --------------------
#     if st.button("Estimate Price 💰"):
#         if is_float(sqft):
#             try:
#                 input_vector = np.zeros(len(data_columns))
#                 input_vector[0] = float(sqft)
#                 input_vector[1] = bath
#                 input_vector[2] = bhk
#                 if location in data_columns:
#                     loc_index = data_columns.index(location)
#                     input_vector[loc_index] = 1
#                 predicted_price = model.predict([input_vector])[0]

#                 st.markdown(
#                     f"""
#                     <div style='background-color: #d4edda; padding: 12px 20px; border-radius: 10px;
#                                 color: black; font-weight: bold; font-size: 18px;
#                                 border-left: 6px solid #28a745; margin-top: 20px;'>
#                         🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#             except Exception as e:
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
#                                 color: black; font-weight: bold; font-size: 16px;
#                                 border-left: 6px solid #dc3545; margin-top: 20px;'>
#                         ❌ Prediction failed: {e}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#         else:
#             st.markdown(
#                 """
#                 <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
#                             color: black; font-weight: bold; font-size: 16px;
#                             border-left: 6px solid #dc3545; margin-top: 20px;'>
#                     ❌ Please enter a valid numeric area (e.g. 1200).
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#     st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# import pickle
# import numpy as np
# import base64
# import json

# # -------------------- Set Background Image --------------------
# def set_bg(jpg_file):
#     with open(jpg_file, "rb") as f:
#         b64_img = base64.b64encode(f.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{b64_img}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}

        
#         .main-box h1 {{
#             color: #222;
#             text-align: center;
#             font-size: 2rem;
#             margin-bottom: 2rem;
#         }}

#         /* Force labels like "Select BHK", "Select Bathrooms" to align left and clean */
#         div[data-testid="stRadio"] > label,
#         div[data-testid="stRadio"] > div > div:first-child > div {{
#             background: none !important;
#             padding: 0 !important;
#             margin-bottom: 8px !important;
#             font-weight: 700 !important;
#             font-size: 1.15rem !important;
#             text-align: left !important;
#             color: black !important;
#             display: block !important;
#             width: 150% !important;
#         }}

#         .stTextInput label, .stSelectbox label {{
#             color: black !important;
#             font-weight: 600 !important;
#             text-align: left !important;
#         }}

#         .stButton>button {{
#             background-color: #f9c74f;
#             color: black;
#             font-weight: bold;
#             border-radius: 10px;
#             width: 100%;
#             height: 3rem;
#             font-size: 1rem;
#         }}

#         .stButton>button:hover {{
#             background-color: #f9844a;
#             color: #FFFFFF;
#         }}

#         /* Radio button options styling */
#         [data-testid="stRadio"] > div {{
#             flex-wrap: wrap !important;
#             gap: 10px;
#         }}

#         [data-testid="stRadio"] label {{
#             background-color: #2c2c2c !important;
#             padding: 12px 20px;
#             border-radius: 10px;
#             border: 2px solid #ccc;
#             color: white !important;
#             font-weight: bold;
#             cursor: pointer;
#             transition: all 0.3s ease;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             min-width: 50px;
#             text-align: center;
#         }}

#         [data-testid="stRadio"] label:hover {{
#             background-color: #444 !important;
#             border-color: #f9c74f;
#             color: #FFFFFF !important;
#         }}

#         [data-testid="stRadio"] input:checked + div {{
#             background-color: #f9844a !important;
#             border-color: #f3722c !important;
#             color: white !important;
#         }}

#         [data-testid="stRadio"] svg {{
#             display: none;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # -------------------- Background Image Path --------------------
# set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\Untitled design.jpg")

# # -------------------- Load Model & Data Columns --------------------
# model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
# data_columns = json.load(open("columns.json", "rb"))['data_columns']
# locations = data_columns[3:]

# def is_float(val):
#     try:
#         float(val)
#         return True
#     except:
#         return False

# # -------------------- Main Layout --------------------
# with st.container():
#     st.markdown('<div class="main-box">', unsafe_allow_html=True)

#     st.markdown('<h1>🏠 Bangalore Home Price Predictor</h1>', unsafe_allow_html=True)

#     sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")

#     bhk = st.radio("Select BHK:", options=[1, 2, 3, 4, 5], horizontal=True, key="selectbhk")
#     bath = st.radio("Select Bathrooms:", options=[1, 2, 3, 4, 5], horizontal=True, key="selectbath")

#     location = st.selectbox("Select Location:", sorted(locations))

#     if st.button("Estimate Price 💰"):
#         if is_float(sqft):
#             try:
#                 input_vector = np.zeros(len(data_columns))
#                 input_vector[0] = float(sqft)
#                 input_vector[1] = bath
#                 input_vector[2] = bhk
#                 if location in data_columns:
#                     loc_index = data_columns.index(location)
#                     input_vector[loc_index] = 1
#                 predicted_price = model.predict([input_vector])[0]
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #d4edda; padding: 12px 20px; border-radius: 10px;
#                                 color: black; font-weight: bold; font-size: 18px;
#                                 border-left: 6px solid #28a745; margin-top: 20px;'>
#                         🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#             except Exception as e:
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
#                                 color: black; font-weight: bold; font-size: 16px;
#                                 border-left: 6px solid #dc3545; margin-top: 20px;'>
#                         ❌ Prediction failed: {e}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#         else:
#             st.markdown(
#                 """
#                 <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
#                             color: black; font-weight: bold; font-size: 16px;
#                             border-left: 6px solid #dc3545; margin-top: 20px;'>
#                     ❌ Please enter a valid numeric area (e.g. 1200).
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#     st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
import pickle
import numpy as np
import base64
import json

# -------------------- Set Background Image --------------------
def set_bg(jpg_file):
    with open(jpg_file, "rb") as f:
        b64_img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .main-box h1 {{
            color: #222;
            text-align: center;
            font-size: 2rem;
            margin-bottom: 2rem;
        }}

        /* Updated label styles */
        .stTextInput label, .stSelectbox label {{
            color: black !important;
            font-weight: 700 !important;
            font-size: 1.15rem !important;
            text-align: left !important;
            display: block !important;
            margin-bottom: 8px !important;
        }}

        div[data-testid="stRadio"] > label,
        div[data-testid="stRadio"] > div > div:first-child > div {{
            background: none !important;
            padding: 0 !important;
            margin-bottom: 8px !important;
            font-weight: 700 !important;
            font-size: 1.15rem !important;
            text-align: left !important;
            color: black !important;
            display: block !important;
        }}

        .stButton>button {{
            background-color: #f9c74f;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            width: 100%;
            height: 3rem;
            font-size: 1rem;
        }}

        .stButton>button:hover {{
            background-color: #f9844a;
            color: #FFFFFF;
        }}

        [data-testid="stRadio"] > div {{
            flex-wrap: wrap !important;
            gap: 10px;
        }}

        [data-testid="stRadio"] label {{
            background-color: #2c2c2c !important;
            padding: 12px 20px;
            border-radius: 10px;
            border: 2px solid #ccc;
            color: white !important;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            min-width: 50px;
            text-align: center;
        }}

        [data-testid="stRadio"] label:hover {{
            background-color: #444 !important;
            border-color: #f9c74f;
            color: #FFFFFF !important;
        }}

        [data-testid="stRadio"] input:checked + div {{
            background-color: #f9844a !important;
            border-color: #f3722c !important;
            color: white !important;
        }}

        [data-testid="stRadio"] svg {{
            display: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------- Background Image Path --------------------
set_bg(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\Untitled design.jpg")

# -------------------- Load Model & Data Columns --------------------
model = pickle.load(open(r"C:\Users\DELL\Desktop\Bengaluru House Price Prediction\banglore_home_prices_model.pickle", "rb"))
data_columns = json.load(open("columns.json", "rb"))['data_columns']
locations = data_columns[3:]

def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

# -------------------- Main Layout --------------------
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)

    st.markdown('<h1 style="color:black;">🏠 Bangalore Home Price Predictor</h1>', unsafe_allow_html=True)


    sqft = st.text_input("Enter Area (in sqft):", placeholder="e.g. 1200")

    bhk = st.radio("Select BHK:", options=[1, 2, 3, 4, 5], horizontal=True, key="selectbhk")
    bath = st.radio("Select Bathrooms:", options=[1, 2, 3, 4, 5], horizontal=True, key="selectbath")

    location = st.selectbox("Select Location:", sorted(locations))

    if st.button("Estimate Price 💰"):
        if is_float(sqft):
            try:
                input_vector = np.zeros(len(data_columns))
                input_vector[0] = float(sqft)
                input_vector[1] = bath
                input_vector[2] = bhk
                if location in data_columns:
                    loc_index = data_columns.index(location)
                    input_vector[loc_index] = 1
                predicted_price = model.predict([input_vector])[0]
                st.markdown(
                    f"""
                    <div style='background-color: #d4edda; padding: 12px 20px; border-radius: 10px;
                                color: black; font-weight: bold; font-size: 18px;
                                border-left: 6px solid #28a745; margin-top: 20px;'>
                        🏷️ Estimated Price: ₹ {round(predicted_price, 2)} Lakhs
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.markdown(
                    f"""
                    <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
                                color: black; font-weight: bold; font-size: 16px;
                                border-left: 6px solid #dc3545; margin-top: 20px;'>
                        ❌ Prediction failed: {e}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.markdown(
                """
                <div style='background-color: #f8d7da; padding: 12px 20px; border-radius: 10px;
                            color: black; font-weight: bold; font-size: 16px;
                            border-left: 6px solid #dc3545; margin-top: 20px;'>
                    ❌ Please enter a valid numeric area (e.g. 1200).
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
