# Week 2 - Task 1: Model Comparison & Evaluation

## 📌 Project Overview

This project focuses on training, evaluating, and comparing three different classification models using the **Titanic Survival Dataset**.

The objective is to determine how different machine learning classification algorithms perform on the same dataset using multiple evaluation metrics and ROC-AUC analysis.

### Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

## 📊 Dataset

**Dataset:** Titanic Survival Dataset

The dataset contains information about Titanic passengers and whether they survived the disaster.

### Target Variable

* `Survived`

  * `0` = Did not survive
  * `1` = Survived

The dataset includes passenger-related features such as age, fare, sex, passenger class, number of siblings/spouses, parents/children, and port of embarkation.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the Titanic dataset using Pandas.
2. Checked the dataset structure and missing values.
3. Renamed the target column from `2urvived` to `Survived`.
4. Removed unnecessary columns such as `Passengerid` and redundant `zero` columns.
5. Handled missing values in the `Embarked` column using the mode.
6. Separated the features (`X`) from the target variable (`y`).
7. Identified categorical columns.
8. Converted categorical variables into numerical form using `OneHotEncoder`.
9. Split the dataset into:

   * 80% training data
   * 20% testing data
10. Used the same processed training and testing data for all three models.

---

## 🤖 Classification Models

### 1. Logistic Regression

Logistic Regression was used as a baseline classification model for predicting whether a passenger survived.

### 2. Decision Tree Classifier

Decision Tree uses a tree-like structure to make classification decisions based on the input features.

### 3. Random Forest Classifier

Random Forest combines multiple decision trees to make predictions and improve classification performance.

---

## 📏 Evaluation Metrics

The models were evaluated using the following metrics:

### Confusion Matrix

The confusion matrix shows:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

### Precision

Measures how many of the passengers predicted as survivors were actually survivors.

### Recall

Measures how many of the actual survivors were correctly identified by the model.

### F1-Score

Provides a combined measure of precision and recall.

### ROC-AUC

Measures the model's ability to distinguish between the two classes.

---

## 📈 ROC Curve Comparison

ROC curves for all three models were plotted on the same graph to visually compare their classification performance.

The ROC curve compares:

* True Positive Rate
* False Positive Rate

**ROC Curve:**
*Add your ROC curve screenshot/image here.*

---

## 📋 Model Comparison Results

The following table summarizes the evaluation results.

> **Note:** Replace all `[ADD YOUR SCORE]` values with the actual results from the Colab notebook.

| Model               |        Precision |           Recall |         F1-Score |          ROC-AUC |
| ------------------- | ---------------: | ---------------: | ---------------: | ---------------: |
| Logistic Regression | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] |
| Decision Tree       | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] |
| Random Forest       | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] | [ADD YOUR SCORE] |

---

## 🏆 Model Selection

Based on the evaluation results, the model selected for deployment was:

**Selected Model: `[ADD MODEL NAME]`**

### Reason

The selected model achieved strong performance based on the evaluation metrics, particularly:

* **Precision:** `[ADD SCORE]`
* **Recall:** `[ADD SCORE]`
* **F1-Score:** `[ADD SCORE]`
* **ROC-AUC:** `[ADD SCORE]`

The final model selection was based on the overall evaluation results rather than relying on a single metric.

---

## 📁 Project Files

```text
week-2/
└── task-1/
    ├── README.md
    └── titanic_model_comparison.ipynb
```

---

## 💻 Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab
* GitHub

---

## 🎯 Key Learning Outcomes

Through this task, I learned how to:

* Train multiple classification models.
* Compare different machine learning algorithms.
* Generate and interpret confusion matrices.
* Calculate precision, recall, and F1-score.
* Calculate ROC-AUC scores.
* Plot and compare multiple ROC curves.
* Select a model based on evaluation results.
* Document and present machine learning experiments professionally.

---

## 🔗 Project Links

**GitHub Repository:**
[ADD YOUR GITHUB REPOSITORY LINK]

**Google Colab Notebook:**
[ADD YOUR COLAB LINK]

---

## 👨‍💻 Internship

This project was completed as part of my **AI/ML Internship at Evolvix**.

**Task:** Week 2 - Task 1: Model Comparison & Evaluation
