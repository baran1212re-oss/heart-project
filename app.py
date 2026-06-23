import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page title
st.title("❤️ Heart Disease Prediction")

st.write("Enter patient information and click Predict.")

# Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", [0, 1])
cp = st.number_input("Chest Pain Type (cp)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.selectbox("Fasting Blood Sugar (fbs)", [0, 1])
restecg = st.number_input("Rest ECG", min_value=0, max_value=2, value=0)
thalach = st.number_input("Maximum Heart Rate", value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("Oldpeak", value=0.0)
slope = st.number_input("Slope", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Major Vessels (ca)", min_value=0, max_value=4, value=0)
thal = st.number_input("Thal", min_value=0, max_value=3, value=2)

# Prediction button
if st.button("Predict"):
    data = np.array([[age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
