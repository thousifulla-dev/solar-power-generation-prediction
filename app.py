import streamlit as st
import numpy as np
import pandas as pd
import pickle  # ← Using pickle instead of joblib

# Load model with pickle
with open("solar_power_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("☀️ Solar Power Generation Prediction")

st.write("Enter environmental values:")

distance = st.number_input("Distance to Solar Noon (radians)", value=0.1)
temperature = st.number_input("Temperature (°C)", value=25.0)
wind_direction = st.number_input("Wind Direction (degrees)", value=180.0)
wind_speed = st.number_input("Wind Speed (m/s)", value=5.0)
sky_cover = st.slider("Sky Cover (0-4)", 0, 4, 1)
visibility = st.number_input("Visibility (km)", value=10.0)
humidity = st.number_input("Humidity (%)", value=50.0)
avg_wind_speed = st.number_input("Average Wind Speed (m/s)", value=5.0)
avg_pressure = st.number_input("Average Pressure (hPa)", value=29.9)

if st.button("Predict"):
    input_data = pd.DataFrame([[
        distance, temperature, wind_direction,
        wind_speed, sky_cover, visibility,
        humidity, avg_wind_speed, avg_pressure
    ]], columns=[
        "distance-to-solar-noon", "temperature", "wind-direction",
        "wind-speed", "sky-cover", "visibility",
        "humidity", "average-wind-speed-(period)", "average-pressure-(period)"
    ])

    prediction = model.predict(input_data)
    st.success(f"Predicted Power: {prediction[0]:.2f} kW")
