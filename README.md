# ⚡️Solar Power Generation Prediction

Regression model to predict solar power output from environmental data. Built as part of ExcelR Data Science Programme.

## Problem Statement
Predict continuous solar power generation using 9 environmental features. Target variable: `Power Generated`.

## Dataset
- **Observations:** 2,920
- **Features:** 9 (Distance to Solar Noon, Temperature, Wind Speed/Direction, Sky Cover, Humidity, Visibility, Pressure)
- **Target:** Power Generated (kW)

## EDA Insights
- Power generation is right-skewed with many zero values (night/cloudy conditions)
- Distance to Solar Noon shows strong negative correlation with power
- Sky Cover and Humidity negatively impact output
- Wind and Pressure have minimal influence

## Model Performance

| Model | MAE | RMSE | R² |
|-------|-----|------|-----|
| Linear Regression | 4,981 | 6,284 | 0.62 |
| Decision Tree | 1,999 | 4,439 | 0.81 |
| Random Forest | 1,548 | 3,407 | 0.89 |
| **Gradient Boosting** | **1,677** | **3,228** | **0.90** |

Gradient Boosting selected for deployment (R² = 0.90).

## Feature Importance
- Distance to Solar Noon: ~84%
- Sky Cover & Humidity: Moderate
- Wind & Pressure: Minimal

## Deployment
Streamlit web app with real-time predictions using joblib-serialized model.

## Tech Stack
Python | Pandas | NumPy | Matplotlib | Seaborn | Scikit-learn | Streamlit | joblib
