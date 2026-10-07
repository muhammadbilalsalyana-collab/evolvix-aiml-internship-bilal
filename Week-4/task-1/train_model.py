import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("train_and_test2.csv")

# Rename target
df = df.rename(columns={"2urvived": "Survived"})

# Remove useless columns
zero_cols = [c for c in df.columns if c.startswith("zero")]
df = df.drop(columns=zero_cols)

# Convert encoded values to readable categories
df["Sex"] = df["Sex"].map({0: "male", 1: "female"})
df["Embarked"] = df["Embarked"].map({0: "C", 1: "Q", 2: "S"})

# Feature engineering
df["FamilySize"] = df["sibsp"] + df["Parch"] + 1
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teen", "YoungAdult", "Adult", "Senior"]
)

features = [
    "Age", "Fare", "Sex", "sibsp", "Parch",
    "Pclass", "Embarked", "FamilySize", "AgeGroup"
]

X = df[features]
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

numeric_features = [
    "Age", "Fare", "sibsp", "Parch", "Pclass", "FamilySize"
]
categorical_features = ["Sex", "Embarked", "AgeGroup"]

numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipe, numeric_features),
    ("cat", categorical_pipe, categorical_features)
])

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=5,
    min_samples_leaf=1,
    random_state=42
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# Train
pipeline.fit(X_train, y_train)

# Test
pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"Test Accuracy: {accuracy:.2%}")

# Save trained model
joblib.dump(pipeline, "model.pkl")
print("model.pkl created successfully.")
