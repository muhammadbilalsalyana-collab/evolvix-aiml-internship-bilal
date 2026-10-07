# Week 4 - Task 1: Serve a Trained Model as a REST API

## Overview

This project serves a trained Titanic Survival Prediction model through a REST API using FastAPI.

The model is a Random Forest Classifier based on the Titanic work from Week 2.

## Dataset

Dataset: `train_and_test2.csv`

Main input features:

- Age
- Fare
- Sex
- sibsp
- Parch
- Pclass
- Embarked
- FamilySize
- AgeGroup

Target:

- Survived: 0 = Not Survived
- Survived: 1 = Survived

## Project Structure

```text
Task-1/
├── app.py
├── train_model.py
├── download_dataset.py
├── model.pkl
├── train_and_test2.csv
├── requirements.txt
├── postman_collection.json
├── sample_request.json
└── README.md
```

## 1. Install Requirements

Open terminal inside this folder:

```bash
pip install -r requirements.txt
```

## 2. Download Dataset

```bash
python download_dataset.py
```

## 3. Train the Model

```bash
python train_model.py
```

This creates:

```text
model.pkl
```

## 4. Start the API

```bash
uvicorn app:app --reload
```

API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /

Checks whether the API is running.

Example response:

```json
{
  "message": "Titanic Survival Prediction API is running"
}
```

### GET /health

Checks API/model health.

Example response:

```json
{
  "status": "healthy",
  "model": "Random Forest"
}
```

### POST /predict

Accepts passenger information and returns the model prediction.

Request:

```json
{
  "Age": 25,
  "Fare": 30.0,
  "Sex": "female",
  "sibsp": 1,
  "Parch": 0,
  "Pclass": 2,
  "Embarked": "S"
}
```

Example response:

```json
{
  "prediction": 1,
  "result": "Survived",
  "confidence": 0.87
}
```

The exact confidence value can change depending on the trained model.

## Input Validation

The API validates:

- Age must be between 0 and 100.
- Fare cannot be negative.
- Pclass must be 1, 2 or 3.
- Sex must be male or female.
- Embarked must be C, Q or S.
- sibsp and Parch must be valid non-negative integers.

Missing required fields are also rejected automatically by FastAPI/Pydantic.

## Postman Testing

Import:

```text
postman_collection.json
```

The collection contains:

1. Home endpoint
2. Health endpoint
3. Valid prediction request
4. Invalid input request

## How Model Serving Works

```text
Client
   |
   | JSON Request
   v
FastAPI
   |
   | Input Validation
   v
Trained Random Forest Model
   |
   | Prediction
   v
JSON Response
```

## Conclusion

The trained Titanic model was successfully wrapped in a FastAPI REST API. The API accepts passenger information in JSON format, validates the input, sends it to the trained model, and returns the predicted survival class with confidence.

## Technologies

- Python
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Random Forest
- Postman
