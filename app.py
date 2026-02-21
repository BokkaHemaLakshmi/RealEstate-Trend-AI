import streamlit as st
import joblib
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Real Estate Trend AI", layout="wide")

# 2. State Management for Dark/Light Mode
if 'mode' not in st.session_state:
    st.session_state.mode = 'Light'

def toggle_mode():
    st.session_state.mode = 'Dark' if st.session_state.mode == 'Light' else 'Light'

# 3. Dynamic Styling (Background + Mode)
# Replace the URL below with any direct link to a house image you like!
bg_img = "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&q=80&w=2070"

if st.session_state.mode == 'Dark':
    main_bg = "rgba(0, 0, 0, 0.7)"
    txt_col = "#ffffff"
else:
    main_bg = "rgba(240, 248, 255, 0.85)"
    txt_col = "#01579b"

st.markdown(f"""
    <style>
    .stApp {{
        background: url("{bg_img}");
        background-size: cover;
        font-weight:bold;
        color:#000000;
    }}
    .main-container {{
        background-color: {main_bg};
        padding: 30px;
        border-radius: 20px;
        color: {txt_col};
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.3);
    }}
    .stButton>button {{
        background-color: lightblue;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Header with Toggle Button on the Right
col_title, col_btn = st.columns([4, 1])
with col_title:
    st.title("Real Estate Price Predictor")
with col_btn:
    st.button(f"🌙 {st.session_state.mode} Mode", on_click=toggle_mode)

# Wrap everything in our styled container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 5. Load Model
model = joblib.load('house_model.joblib')
features = joblib.load('features.joblib')

# 6. UI Layout
st.subheader("Property Characteristics & Amenities")
c1, c2 = st.columns(2)
with c1:
    qual = st.slider("Overall Quality (1-10)", 1, 10, 6)
    gr_area = st.number_input("Living Area (Sq Ft)", value=1500)
    garage = st.number_input("Garage Cars", 0, 4, 2)
with c2:
    bsmt = st.number_input("Total Basement (Sq Ft)", value=1000)
    bath = st.slider("Full Bathrooms", 1, 4, 2)
    fireplaces = st.slider("Fireplaces", 0, 3, 1)

ac = st.checkbox("Central Air Conditioning")

if st.button("Calculate Market Value"):
    ac_val = 1 if ac else 0
    input_data = np.array([[qual, gr_area, garage, bsmt, bath, fireplaces, ac_val]])
    prediction = model.predict(input_data)[0]
    
    st.markdown(f"## Estimated Value: :blue[${prediction:,.2f}]")

st.markdown('</div>', unsafe_allow_html=True)
