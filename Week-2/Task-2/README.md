## Model Performance & Results

The Task 2 model was developed by applying feature engineering and hyperparameter tuning to the Random Forest classifier used as the Task 1 baseline.

### Feature Engineering

Two new features were created from the Titanic dataset:

* **FamilySize** — calculated using `SibSp + Parch + 1`
* **AgeGroup** — created by grouping passengers into Child, Teen, Adult, and Senior categories based on age.

These engineered features were included in the model along with the original relevant features.

### Hyperparameter Tuning

`GridSearchCV` with 5-fold cross-validation was used to find the best Random Forest configuration.

**Best Parameters:**

```text
max_depth = 5
min_samples_leaf = 1
min_samples_split = 5
n_estimators = 100
```

### Before vs After Performance

| Model                         |                    Accuracy |
| ----------------------------- | --------------------------: |
| Task 1 Baseline Random Forest |                  **75.95%** |
| Task 2 Tuned Random Forest    |                  **77.10%** |
| **Improvement**               | **+1.15 percentage points** |

The tuned Random Forest achieved an accuracy of **77.10%**, compared with **75.95%** for the Task 1 baseline. This represents an improvement of **1.15 percentage points** on the test set.

### Conclusion

Feature engineering and hyperparameter tuning resulted in a measurable improvement in the Random Forest model's test accuracy. The combination of the new `FamilySize` and `AgeGroup` features with the optimized Random Forest parameters improved the model from **75.95% to 77.10%**.
