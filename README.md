.

# 🚘 Resale Car Price Prediction App

## This project focuses on predicting the resale price of cars, helping both sellers and buyers estimate a fair market value based on car features. The model analyzes historical data and provides accurate price predictions through a user-friendly web application.

# 📊 Dataset & Preprocessing

## Initially contained 86 features and 1 target variable (price)

# Derived new features from existing data:

## Car Age – calculated from the car’s manufacturing year

## Car Size – derived based on vehicle dimensions/category

# Data cleaning steps included:

## Removing null values and duplicate records

## Dropping empty rows and unwanted features

# Filling missing values:

## Numerical features → Median & Mode

## Categorical features → Mode

## Outlier removal using the IQR (Interquartile Range) method

## Encoding categorical variables using Label Encoding

# ⚙️ Feature Engineering

## Split data into features (X) and target (y)

## Applied StandardScaler to scale feature values for improved model performance

# 🤖 Machine Learning Models Used

## Multiple machine learning algorithms were trained and evaluated:

## Linear Regression

## Decision Tree

## Support Vector Machine (SVM)

## K-Nearest Neighbors (KNN)

## Random Forest Regressor

## ✅ Random Forest Regression was selected as the final model as it achieved the highest accuracy of 86%.

# 📈 Model Evaluation

## The model performance was evaluated using:

## Mean Squared Error (MSE)

## Mean Absolute Error (MAE)

## Root Mean Squared Error (RMSE)

## R² Score

# 🛠️ Technologies & Libraries

## Python

## Pandas, NumPy

## Matplotlib, Seaborn

## Scikit-learn

## Streamlit

## Pickle

# 🌐 Web Application

## Developed an interactive Streamlit web application

## Allows users to input car details and receive real-time resale price predictions

## The trained machine learning model was saved using pickle and integrated into the frontend

# 🎯 Conclusion

## This Resale Car Price Prediction App demonstrates an end-to-end machine learning workflow, including feature engineering (Car Age & Car Size), model selection, evaluation, and deployment using Streamlit.
