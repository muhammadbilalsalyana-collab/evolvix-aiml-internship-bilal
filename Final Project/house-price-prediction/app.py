
import streamlit as st
import pandas as pd
import joblib
import gzip
from pathlib import Path

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction App")
st.write(
    "Estimate California district median house values "
    "using Machine Learning."
)

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "best_model.joblib.gz"
METRICS_PATH = BASE_DIR / "model_metrics.csv"

# Load compressed model
if not MODEL_PATH.exists():
    st.error("Model file missing: best_model.joblib.gz")
    st.stop()

try:
    with gzip.open(MODEL_PATH, "rb") as file:
        model = joblib.load(file)
except Exception as error:
    st.error(f"Could not load model: {error}")
    st.stop()

# Show evaluation metrics
if METRICS_PATH.exists():
    st.subheader("📊 Model Evaluation")
    metrics = pd.read_csv(METRICS_PATH)
    st.dataframe(metrics, use_container_width=True)

st.subheader("🏡 Enter Property and Area Details")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        income = st.number_input(
            "Median Income (dataset units)",
            min_value=0.1,
            max_value=20.0,
            value=5.0
        )

        age = st.number_input(
            "House Age (years)",
            min_value=1.0,
            max_value=100.0,
            value=20.0
        )

        rooms = st.number_input(
            "Average Rooms",
            min_value=1.0,
            max_value=100.0,
            value=5.0
        )

        bedrooms = st.number_input(
            "Average Bedrooms",
            min_value=0.1,
            max_value=20.0,
            value=1.0
        )

    with col2:
        population = st.number_input(
            "Area Population",
            min_value=1.0,
            max_value=50000.0,
            value=1000.0
        )

        occupancy = st.number_input(
            "Average Occupancy",
            min_value=0.1,
            max_value=100.0,
            value=3.0
        )

        latitude = st.number_input(
            "Latitude",
            min_value=32.0,
            max_value=42.0,
            value=34.0
        )

        longitude = st.number_input(
            "Longitude",
            min_value=-125.0,
            max_value=-114.0,
            value=-118.0
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
                "Please review the input values."
            )
        else:
            estimated_value = prediction * 100000

            st.success("Prediction generated successfully!")

            st.metric(
                "Estimated Median District House Value",
                f"${estimated_value:,.0f}"
            )

            st.info(
                "This is an estimated median value for a California "
                "district, not the exact market price of an individual house."
            )

    except (ValueError, TypeError, KeyError) as error:
        st.error(f"Prediction error: {error}")

st.divider()

st.caption(
    "Built with Python, Pandas, Scikit-learn and Streamlit | "
    "Evolvix AI/ML Capstone Project"
)

