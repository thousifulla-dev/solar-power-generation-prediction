
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("solar_power_model.pkl")

st.title("Solar Power Generation Prediction")

st.write("Enter environmental values:")

distance = st.number_input("Distance to Solar Noon (radians)", value=0.1)
temperature = st.number_input("Temperature", value=25.0)
wind_direction = st.number_input("Wind Direction", value=180.0)
wind_speed = st.number_input("Wind Speed", value=5.0)
sky_cover = st.slider("Sky Cover (0-4)", 0, 4, 1)
visibility = st.number_input("Visibility", value=10.0)
humidity = st.number_input("Humidity", value=50.0)
avg_wind_speed = st.number_input("Average Wind Speed", value=5.0)
avg_pressure = st.number_input("Average Pressure", value=29.9)

if st.button("Predict"):
    input_data = np.array([[distance, temperature, wind_direction,
                            wind_speed, sky_cover, visibility,
                            humidity, avg_wind_speed, avg_pressure]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Power: {prediction[0]:.2f} Joules")
