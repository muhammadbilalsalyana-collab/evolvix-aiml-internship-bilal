from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="REST API for a trained Titanic Random Forest model.",
    version="1.0"
)

model = joblib.load("model.pkl")


class Passenger(BaseModel):
    Age: float = Field(..., ge=0, le=100)
    Fare: float = Field(..., ge=0)
    Sex: str
    sibsp: int = Field(..., ge=0, le=20)
    Parch: int = Field(..., ge=0, le=20)
    Pclass: int = Field(..., ge=1, le=3)
    Embarked: str


@app.get("/")
def home():
    return {"message": "Titanic Survival Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy", "model": "Random Forest"}


@app.post("/predict")
def predict(passenger: Passenger):
    if passenger.Sex.lower() not in ["male", "female"]:
        return {"error": "Sex must be male or female"}

    if passenger.Embarked.upper() not in ["C", "Q", "S"]:
        return {"error": "Embarked must be C, Q or S"}

    data = passenger.model_dump()
    data["Sex"] = data["Sex"].lower()
    data["Embarked"] = data["Embarked"].upper()

    # Same feature engineering used during training
    data["FamilySize"] = data["sibsp"] + data["Parch"] + 1

    age = data["Age"]
    if age <= 12:
        data["AgeGroup"] = "Child"
    elif age <= 18:
        data["AgeGroup"] = "Teen"
    elif age <= 35:
        data["AgeGroup"] = "YoungAdult"
    elif age <= 60:
        data["AgeGroup"] = "Adult"
    else:
        data["AgeGroup"] = "Senior"

    df = pd.DataFrame([data])

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][prediction])

    result = "Survived" if prediction == 1 else "Not Survived"

    return {
        "prediction": prediction,
        "result": result,
        "confidence": round(probability, 4)
    }
