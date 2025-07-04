# requirements.py
# List of required Python packages for the Bangalore House Price Prediction Streamlit App

# Streamlit is used to build the interactive web app interface
import streamlit as st

# NumPy is used for creating and manipulating numerical arrays
import numpy as np

# Pickle is used for loading the trained machine learning model and column list
import pickle

# scikit-learn is the ML library used to build and train the regression model
from sklearn.linear_model import LinearRegression

# pandas may be used during model training or column data generation
import pandas as pd

# base64 is used to encode images for background embedding in Streamlit via HTML
import base64
