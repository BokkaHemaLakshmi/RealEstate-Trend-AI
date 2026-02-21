import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Real Estate Trend AI", layout="centered")

# Custom CSS for the "Sky Blue" theme
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #87CEEB; color: white; border-radius: 10px; width: 100%; }
    .prediction-box { background-color: #e1f5fe; padding: 20px; border-radius: 15px; border: 2px solid #87CEEB; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. Load the trained brain
@st.cache_resource
def load_model():
    model = joblib.load('house_model.joblib')
    features = joblib.load('features.joblib')
    return model, features

model, features = load_model()

st.title("🏙️ Real Estate Price Predictor")
st.write("Analysis based on Ames Housing Data Trend")

# 3. Create Input Fields
st.subheader("Property Details")
col1, col2 = st.columns(2)

with col1:
    qual = st.slider("Overall Quality (1-10)", 1, 10, 6)
    gr_area = st.number_input("Living Area (Sq Ft)", value=1500)
    garage = st.number_input("Garage Cars", 0, 4, 2)

with col2:
    bsmt = st.number_input("Total Basement (Sq Ft)", value=1000)
    bath = st.slider("Full Bathrooms", 1, 4, 2)
    fireplaces = st.slider("Fireplaces", 0, 3, 1)

ac = st.checkbox("Central Air Conditioning")

# 4. Prediction Logic
if st.button("Calculate Market Value"):
    ac_val = 1 if ac else 0
    # Data must be in same order as 'features'
    input_data = np.array([[qual, gr_area, garage, bsmt, bath, fireplaces, ac_val]])
    
    prediction = model.predict(input_data)[0]
    
    st.markdown(f"""
        <div class="prediction-box">
            <h3 style='color: #0277bd;'>Estimated Property Value</h3>
            <h2 style='color: #01579b;'>${prediction:,.2f}</h2>
        </div>
    """, unsafe_allow_html=True)
