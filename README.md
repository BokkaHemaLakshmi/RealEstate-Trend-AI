# RealEstate-Trend-AI
AI-powered Real Estate Price Prediction App using XGBoost and Streamlit. Features 89% accuracy (R²: 0.8924) on the Ames Housing Dataset.  Topics: machine-learning, python, xgboost, data-science, real-estate-analysis, streamlit
# 🏙️ Real Estate Price Trend Analysis & Prediction

This project uses Machine Learning to analyze and predict house prices based on the Ames Housing Dataset. It features a trained **XGBoost Regressor** model and a **Sky Blue** themed web interface for real-time predictions.

## 🚀 Live Demo
[Paste your Streamlit Link Here]

## 📊 Model Performance
For my UGC Research Paper, the model was evaluated using standard metrics:
* **R-Squared (R²):** 0.8924 (High Predictive Power)
* **MAE:** $20,532.00
* **Algorithm:** XGBoost (Extreme Gradient Boosting)

## 🛠️ Key Features
- **Overall Quality:** Predictive analysis based on material and finish.
- **Amenity Impact:** Calculates value added by Central Air, Fireplaces, and Garage capacity.
- **Interactive UI:** Built with Streamlit for a seamless user experience.

## 📂 Project Structure
- `app.py`: The Streamlit web application.
- `house_model.joblib`: The trained XGBoost model.
- `features.joblib`: Serialized list of features for consistency.
- `requirements.txt`: Necessary libraries for deployment.

## 📝 How to Run Locally
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/RealEstate-Trend-AI.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
