import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))

# Title
st.title(" Car Price Prediction App")

st.write("Enter car details to predict price")

# User Inputs
name = st.text_input("Car Name (e.g. Maruti Swift)")
company = st.text_input("Company (e.g. Maruti)")
year = st.number_input("Year", min_value=1990, max_value=2025)
kms_driven = st.number_input("Kilometers Driven")
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG", "CNG"])

# Prediction button
if st.button("Predict Price"):
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_df)

    st.success(f" Estimated Price: ₹ {int(prediction[0]):,}")