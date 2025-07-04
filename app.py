import streamlit as st
import pickle
import numpy as np
import base64
import json

# -------------------- Set Background Image --------------------
def set_bg(jpeg_file):
    with open(jpeg_file, "rb") as f:
        b64_img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Apply white block behind main content */
        section.main > div:has(.block-container) {{
            display: flex;
            justify-content: center;
        }}

        .block-container {{
            background-color: rgba(255, 255, 255, 0.97);
            padding: 3rem 2.5rem;
            border-radius: 25px;
            max-width: 750px;
            width: 100%;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.2);
        }}

       

        h1 {{
            color: #222;
            text-align: center;
            font-size: 2rem;
            margin-bottom: 2rem;
        }}

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
set_bg('Background.jpeg')

# -------------------- Load Model & Data Columns --------------------
model = pickle.load(open("banglore_home_prices_model.pickle", "rb"))
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
