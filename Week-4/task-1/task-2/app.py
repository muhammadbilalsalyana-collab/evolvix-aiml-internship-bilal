
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Titanic Predictor", page_icon="🚢")

@st.cache_resource
def load_model():
    return joblib.load("titanic_logistic_regression.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details to predict survival.")

st.info(
    "This app provides an educational prediction. "
    "Results are estimates and may be incorrect."
)

with st.form("prediction_form"):
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Gender", ["male", "female"])
    age = st.slider("Age", 1, 80, 25)
    sibsp = st.number_input("Siblings/Spouses", 0, 8, 0)
    parch = st.number_input("Parents/Children", 0, 6, 0)
    fare = st.number_input("Ticket Fare", min_value=0.0, value=30.0)
    embarked = st.selectbox("Embarkation Port", ["S", "C", "Q"])

    predict = st.form_submit_button("Predict Survival")

if predict:
    data = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked,
        "sibsp": sibsp
    }])

    expected = getattr(model, "feature_names_in_", None)

    if expected is not None:
        missing = [c for c in expected if c not in data.columns]

        if missing:
            st.error(
                "Model input features do not match the app. "
                f"Missing: {missing}"
            )
            st.stop()

        data = data[list(expected)]

    try:
        result = model.predict(data)[0]

        if result == 1:
            st.success("Prediction: Passenger may have survived.")
        else:
            st.error("Prediction: Passenger may not have survived.")

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(data)[0]
            st.write(
                f"Estimated survival probability: "
                f"{probability[list(model.classes_).index(1)] * 100:.2f}%"
            )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.write(
            "The model's input columns or preprocessing may differ "
            "from the app. Check the original training code."
        )
