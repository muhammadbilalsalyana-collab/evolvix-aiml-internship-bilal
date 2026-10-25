
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction App")
st.write(
    "Estimate California district median house values "
    "using a machine learning model."
)

MODEL_PATH = Path(__file__).parent / "best_model.joblib"
METRICS_PATH = Path(__file__).parent / "model_metrics.csv"

if not MODEL_PATH.exists():
    st.error("Model file is missing. Add best_model.joblib.")
    st.stop()

model = joblib.load(MODEL_PATH)

if METRICS_PATH.exists():
    metrics = pd.read_csv(METRICS_PATH)
    st.subheader("Model Evaluation")
    st.dataframe(metrics, use_container_width=True)

st.subheader("Enter Property and Area Details")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        income = st.number_input(
            "Median Income (dataset units)",
            min_value=0.1, max_value=20.0, value=5.0
        )
        age = st.number_input(
            "House Age (years)",
            min_value=1.0, max_value=100.0, value=20.0
        )
        rooms = st.number_input(
            "Average Rooms",
            min_value=1.0, max_value=100.0, value=5.0
        )
        bedrooms = st.number_input(
            "Average Bedrooms",
            min_value=0.1, max_value=20.0, value=1.0
        )

    with col2:
        population = st.number_input(
            "Area Population",
            min_value=1.0, max_value=50000.0, value=1000.0
        )
        occupancy = st.number_input(
            "Average Occupancy",
            min_value=0.1, max_value=100.0, value=3.0
        )
        latitude = st.number_input(
            "Latitude",
            min_value=32.0, max_value=42.0, value=34.0
        )
        longitude = st.number_input(
            "Longitude",
            min_value=-125.0, max_value=-114.0, value=-118.0
        )

    submitted = st.form_submit_button(
        "Predict House Value",
        use_container_width=True
    )

if submitted:
    input_data = pd.DataFrame([{
        "MedInc": income,
        "HouseAge": age,
        "AveRooms": rooms,
        "AveBedrms": bedrooms,
        "Population": population,
        "AveOccup": occupancy,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    try:
        prediction = float(model.predict(input_data)[0])

        if prediction <= 0:
            st.warning(
                "The model returned a non-positive estimate. "
                "Try reviewing the inputs."
            )
        else:
            estimated_value = prediction * 100000

            st.success("Prediction generated successfully!")
            st.metric(
                "Estimated Median District House Value",
                f"${estimated_value:,.0f}"
            )
            st.caption(
                "This is a model estimate for a California district, "
                "not an exact price for an individual house."
            )

    except (ValueError, TypeError) as error:
        st.error(f"Could not generate prediction: {error}")

st.divider()
st.caption(
    "Built with Python, Scikit-learn and Streamlit | "
    "Evolvix AI/ML Capstone Project"
)
