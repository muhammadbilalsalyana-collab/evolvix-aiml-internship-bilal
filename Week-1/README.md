# Titanic Dataset — Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset using Python.

The goal is to clean the dataset, explore passenger information using statistical analysis and visualizations, and identify important patterns related to passenger survival.

## Dataset

The Titanic dataset contains information about passengers, including:

- Passenger ID
- Age
- Sex
- SibSp
- Parch
- Pclass
- Fare
- Embarked
- Survived

## Data Cleaning

The following data-cleaning steps were performed:

- Checked for missing values.
- Filled missing values in the `Embarked` column using the mode.
- Checked for duplicate records.
- Checked data types and dataset information.
- Generated summary statistics.

## Exploratory Data Analysis

The following visualizations were created:

1. Survival Count
2. Survival by Gender
3. Age Distribution
4. Survival by Passenger Class
5. Fare Distribution by Survival

## Key Insights

1. The number of passengers who did not survive was significantly higher than the number of passengers who survived.

2. Survival varied between male and female passengers, indicating that gender was an important factor associated with survival.

3. Passenger class and ticket fare were associated with survival. Passengers in higher classes and those paying higher fares generally had better survival outcomes.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Conclusion

The analysis shows that passenger survival was associated with several factors, including gender, passenger class, and fare. Exploratory Data Analysis helped identify these patterns through statistical analysis and visualization.
