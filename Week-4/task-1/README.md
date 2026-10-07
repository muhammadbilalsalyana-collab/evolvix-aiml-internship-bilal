# Week 4 - Task 1: Titanic Survival Prediction API

## Overview

This project serves a trained **Titanic Survival Prediction model** as a REST API using **FastAPI**.

The model is a **Random Forest Classifier** trained on Titanic passenger data. The API accepts passenger information and predicts whether the passenger survived or not.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pandas
* Scikit-learn
* Random Forest
* Joblib
* Postman

## Project Structure

```text
week-4-task-1/
│
├── app.py
├── train_model.py
├── download_dataset.py
├── requirements.txt
├── postman_collection.json
├── sample_request.json
├── .gitignore
└── README.md
```

## Dataset

The project uses the Titanic dataset.

### Features

* Age
* Fare
* Sex
* sibsp
* Parch
* Pclass
* Embarked
* FamilySize
* AgeGroup

### Target

* `0` = Not Survived
* `1` = Survived

## Installation

Open the terminal inside the project folder and install the required libraries:

```bash
pip install -r requirements.txt
```

## Download Dataset

Run:

```bash
python download_dataset.py
```

This downloads `train_and_test2.csv`.

## Train the Model

Run:

```bash
python train_model.py
```

This trains the Random Forest model and creates:

```text
model.pkl
```

## Run the FastAPI Server

Start the API using:

```bash
uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger API Documentation

FastAPI provides automatic API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

From there, the API endpoints can be tested directly in the browser.

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

Checks the API and model status.

Example response:

```json
{
  "status": "healthy",
  "model": "Random Forest"
}
```

### POST /predict

Predicts Titanic passenger survival.

Example request:

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

The confidence value may change depending on the trained model.

## Input Validation

The API validates passenger information before making a prediction.

Examples:

* Age must be between 0 and 100.
* Fare cannot be negative.
* Pclass must be 1, 2, or 3.
* Sex must be `male` or `female`.
* Embarked must be `C`, `Q`, or `S`.
* `sibsp` and `Parch` must be non-negative integers.

## Postman Testing

The project includes:

```text
postman_collection.json
```

Import this file into Postman to test the API.

The collection includes:

1. Home endpoint
2. Health endpoint
3. Valid prediction request
4. Invalid input request

## How It Works

```text
Passenger Data
      ↓
FastAPI
      ↓
Input Validation
      ↓
Feature Engineering
      ↓
Random Forest Model
      ↓
Prediction + Confidence
      ↓
JSON Response
```

## Model

A **Random Forest Classifier** is used for prediction.

The model uses preprocessing for numerical and categorical features and performs feature engineering using:

* FamilySize
* AgeGroup

The trained pipeline is saved as:

```text
model.pkl
```

## Conclusion

This project demonstrates how a trained machine learning model can be deployed as a REST API using FastAPI.

The API receives passenger information, validates the input, performs the required feature engineering, sends the data to the Random Forest model, and returns the predicted survival result with confidence.

## Author

**Muhammad Bilal**

Week 4 - Task 1
AI/ML Internship
