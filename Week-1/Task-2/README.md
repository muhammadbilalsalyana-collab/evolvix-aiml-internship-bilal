# Task 2 — First Machine Learning Model

## Project Overview

This project is part of the **EvolviX AI/ML Internship — Week 1**.

The goal of this task was to build, train, evaluate, and save a baseline Machine Learning model using the **Titanic dataset**.

For this project, I used **Logistic Regression** to predict whether a passenger survived the Titanic disaster based on available passenger information.

---

## Objective

The main objectives of this project were:

* Prepare the dataset for Machine Learning.
* Handle missing values and categorical data.
* Split the data into training and testing sets.
* Train a baseline classification model using Scikit-learn.
* Evaluate the model using classification metrics.
* Save the trained model using Joblib.

---

## Dataset

The **Titanic dataset** contains information about passengers, including features such as:

* Age
* Fare
* Sex
* Passenger Class
* SibSp
* Parch
* Embarked

### Target Variable

**Survived**

* `0` = Did not survive
* `1` = Survived

This makes the project a **binary classification problem**.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Checked the dataset structure and missing values.
2. Handled missing values in the `Embarked` column using the mode.
3. Removed unnecessary columns that did not provide useful information.
4. Separated the features (`X`) from the target (`y`).
5. Identified numerical and categorical columns.
6. Applied `StandardScaler` to numerical features.
7. Applied `OneHotEncoder` to categorical features.

A Scikit-learn `Pipeline` and `ColumnTransformer` were used to keep preprocessing and model training organized and help prevent data leakage.

---

## Train/Test Split

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

`random_state=42` was used to make the results reproducible.

`stratify=y` was also used to maintain the class distribution between the training and testing datasets.

---

## Machine Learning Model

### Logistic Regression

A **Logistic Regression** model was used as the baseline classification model.

The model learns patterns from the training data and predicts whether a passenger survived or did not survive.

```text
Passenger Information
        ↓
Data Preprocessing
        ↓
Logistic Regression
        ↓
Survived / Did Not Survive
```

---

## Evaluation Metrics

The model was evaluated using the following metrics:

### Accuracy

Accuracy represents the percentage of total predictions that were correct.

### Precision

Precision shows how many of the passengers predicted as survivors actually survived.

### Recall

Recall shows how many of the passengers who actually survived were correctly identified by the model.

### F1 Score

F1 Score provides a balance between precision and recall.

---

## Results

The model was evaluated on **262 test samples**.

| Metric    | Score |
| --------- | ----: |
| Accuracy  |  0.83 |
| Precision |  0.70 |
| Recall    |  0.59 |
| F1 Score  |  0.64 |

### Results Interpretation

The Logistic Regression model achieved an **accuracy of 83%**, meaning that it correctly predicted approximately 83% of the test cases.

The model performed better at identifying passengers who did not survive than passengers who survived. For the survival class, the model achieved a precision of 70% and a recall of 59%.

Overall, this model provides a good **baseline classification model** for the Titanic dataset.

---

## Model Saving

The trained model was saved using **Joblib**.

Saved model file:

```text
titanic_logistic_regression.pkl
```

This file can be loaded later to make predictions without training the model again.

---

## Project Files

```text
week-1/
└── task-2/
    ├── README.md
    ├── titanic_classification.ipynb
    └── titanic_logistic_regression.pkl
```

### Files Description

* `README.md` — Project documentation and results.
* `titanic_classification.ipynb` — Google Colab notebook containing preprocessing, training, prediction, and evaluation.
* `titanic_logistic_regression.pkl` — Saved trained Logistic Regression model.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Google Colab

---

## Key Learning Outcomes

Through this task, I learned how to:

* Prepare data for Machine Learning.
* Handle categorical and numerical features.
* Perform a proper train/test split.
* Avoid data leakage using preprocessing pipelines.
* Train a Logistic Regression classification model.
* Evaluate a model using Accuracy, Precision, Recall, and F1 Score.
* Save a trained Machine Learning model using Joblib.

---

## Conclusion

This project helped me understand the complete basic Machine Learning workflow, from data preprocessing and train/test splitting to model training, evaluation, and model saving.

The Logistic Regression baseline model achieved **83% accuracy** on the test dataset and provided a strong starting point for further model improvement.
