# 🏠 House Price Prediction

### End-to-End Machine Learning Application

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://evolvix-aiml-internship-bilal-8ivss5a8f45sbbrys8krab.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Deployed-success)](https://evolvix-aiml-internship-bilal-8ivss5a8f45sbbrys8krab.streamlit.app/)

**Evolvix | AI/ML Internship Capstone Project**

An end-to-end machine learning project that estimates **median house values in California districts** from housing, demographic, and geographic features. A trained Random Forest model is served through an interactive Streamlit web application.

### 🔗 **[Try the Live App →](https://evolvix-aiml-internship-bilal-8ivss5a8f45sbbrys8krab.streamlit.app/)**

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Key Features](#-key-features)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Model Performance](#-model-performance)
- [Technical Stack](#-technical-stack)
- [Repository Structure](#-repository-structure)
- [Run Locally](#-run-locally)
- [Usage & Example Predictions](#-usage--example-predictions)
- [Deployment Notes](#-deployment-notes)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Project Overview

Estimating housing value is a classic **supervised regression** problem influenced by income levels, housing characteristics, population density, and location. This project trains and compares two regression models on the California Housing dataset, selects the better performer, and deploys it as a public web app where anyone can enter district-level details and receive an instant estimate.

| | |
|---|---|
| **Problem Type** | Supervised Learning, Regression |
| **Dataset** | California Housing (scikit-learn) |
| **Models Compared** | Linear Regression, Random Forest Regressor |
| **Selected Model** | Random Forest Regressor |
| **Interface** | Streamlit |
| **Deployment** | Streamlit Community Cloud |

## 🚀 Live Demo

**App:** https://evolvix-aiml-internship-bilal-8ivss5a8f45sbbrys8krab.streamlit.app/

> The app may take a few seconds to wake up if it has been idle, since it runs on Streamlit Community Cloud.

## ✨ Key Features

- Interactive form with eight input fields and built-in range validation
- Real-time predictions from a trained Random Forest model
- Model evaluation table (MAE, RMSE, R²) displayed inside the app
- Compressed model artifact (`.joblib.gz`) for lightweight deployment
- Clear user-facing messages for invalid or unrealistic outputs

## 📊 Dataset

The project uses the **[California Housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)**, which contains district-level census data.

| Feature | Description |
|---|---|
| `MedInc` | Median income in the district (in tens of thousands of USD) |
| `HouseAge` | Median age of houses in the district |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | District population |
| `AveOccup` | Average number of household members |
| `Latitude` | District latitude |
| `Longitude` | District longitude |

**Target:** Median house value, expressed in units of $100,000. The app multiplies the prediction by 100,000 to display it in US dollars.

## 🔬 Methodology

1. **Data exploration:** examine feature distributions and relationships.
2. **Preprocessing:** prepare features and split data into training and test sets.
3. **Model training:** train Linear Regression (baseline) and Random Forest Regressor.
4. **Evaluation:** compare models using MAE, RMSE, and R².
5. **Model selection:** choose the best-performing model.
6. **Serialization:** save the model with Joblib (gzip-compressed).
7. **Application development:** build the Streamlit interface around the saved model.
8. **Deployment:** publish on Streamlit Community Cloud and verify predictions.

**Final model configuration:**

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=18,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
)
```

## 📈 Model Performance

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| **Random Forest** ✅ | **0.3277** | **0.5057** | **0.8048** |

*MAE and RMSE are in units of $100,000, so Random Forest's MAE of 0.3277 corresponds to an average error of roughly $32,800.*

**Takeaway:** Random Forest reduces MAE by about 39% and explains about 80% of the variance in house values, compared to about 58% for the linear baseline. This indicates that the relationship between location, income, and housing value is non-linear, which tree-based ensembles capture better.

Full results are stored in [`model_metrics.csv`](./model_metrics.csv).

## 🛠️ Technical Stack

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Web Application | Streamlit |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |

## 📂 Repository Structure

```text
house-price-prediction/
├── app.py                  # Streamlit application
├── best_model.joblib.gz    # Trained Random Forest model (compressed)
├── model_metrics.csv       # Evaluation metrics for both models
├── requirements.txt        # Pinned dependencies
└── README.md               # Project documentation
```

## 💻 Run Locally

**Prerequisites:** Python 3.12 and pip.

**1. Clone the repository**

```bash
git clone https://github.com/muhammadbilalsalyana-collab/evolvix-aiml-internship-bilal.git
cd evolvix-aiml-internship-bilal/Final_Project/house-price-prediction
```

**2. (Recommended) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Launch the app**

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

> ⚠️ **Version note:** The model was trained with scikit-learn **1.6.1**. Loading it with a different version may cause warnings or incorrect behavior, which is why exact versions are pinned in `requirements.txt`.

## 🧪 Usage & Example Predictions

1. Open the [live app](https://evolvix-aiml-internship-bilal-8ivss5a8f45sbbrys8krab.streamlit.app/).
2. Enter the district details in the form.
3. Click **Predict House Value**.
4. Read the estimated median house value for the district.

**Sample inputs and outputs:**

| Scenario | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Lat | Lon | Estimate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Default values | 5.0 | 20 | 5.0 | 1.0 | 1000 | 3.0 | 34.00 | -118.00 | ~$206,000 |
| High-income coastal area | 9.0 | 15 | 7.0 | 1.0 | 1500 | 2.5 | 34.05 | -118.40 | ~$462,000 |
| Lower-income area | 1.5 | 40 | 4.0 | 1.1 | 2500 | 4.0 | 34.00 | -118.20 | ~$150,000 |

## ☁️ Deployment Notes

- Hosted on **Streamlit Community Cloud**, deployed from the `main` branch.
- Python version is set to **3.12** in the deployment's advanced settings.
- Folder names avoid spaces, because spaces in paths can break dependency installation on Streamlit Cloud.
- Dependencies are pinned in `requirements.txt` to match the environment used for training.

## ⚠️ Limitations

- Predictions are **district-level median values**, not prices for individual properties.
- The dataset is based on 1990 California census data, so values do not reflect current market prices.
- The model only generalizes to California and to feature ranges similar to its training data.
- This is an educational prototype and is not a substitute for professional property valuation.

## 🔮 Future Improvements

- Hyperparameter tuning with cross-validation and comparison with gradient boosting models
- Feature importance and prediction explanation charts in the app
- Interactive map visualization for latitude and longitude inputs
- Automated tests and CI for the application
- Evaluation on more recent housing data

## 👨‍💻 Author

**Muhammad Bilal**
AI/ML Intern at Evolvix

- GitHub: [@muhammadbilalsalyana-collab](https://github.com/muhammadbilalsalyana-collab)
- Repository: [evolvix-aiml-internship-bilal](https://github.com/muhammadbilalsalyana-collab/evolvix-aiml-internship-bilal)

## 🙏 Acknowledgements

Thanks to **Evolvix** for the internship opportunity and guidance, and to the **scikit-learn** and **Streamlit** communities for their excellent tools and documentation.

---

⭐ *If you found this project useful, consider giving the repository a star.*
Bilal
AI/ML Internship Capstone — Evolvix

Developed as an end-to-end machine learning prototype for the Evolvix AI/ML Internship Program.
