# Diabetes Analysis Project

This project aims to detect diabetes using a dataset originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict, based on diagnostic measurements, whether a patient has diabetes. The dataset focuses on female patients of Pima Indian heritage, who are at least 21 years old.

## Project Objectives

1. **Data Exploration and Preprocessing**: Understanding the dataset and cleaning the data to ensure it is suitable for modeling.
2. **Feature Selection**: Identifying the most relevant features that contribute to predicting diabetes.
3. **Model Development**: Developing and training a logistic regression model to predict the outcome.
4. **Model Evaluation**: Evaluating the model's performance using appropriate metrics to ensure its accuracy and reliability.

## Dataset

The dataset contains several features related to diabetes diagnostics, including:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function
- **Age**: Age (years)
- **Outcome**: Class variable (0 or 1)

The data was collected with several constraints to ensure that all patients are females at least 21 years old of Pima Indian heritage.

## Methodology

1. **Data Loading**: The data is loaded into a pandas DataFrame.
2. **Data Splitting**: The dataset is split into training and testing sets.
3. **Model Training**: A logistic regression model is trained using the training data.
4. **Prediction**: The trained model is used to predict the outcome based on new input values.
5. **Evaluation**: The model's performance is evaluated using metrics like accuracy, precision, and recall.

## Conclusion

This project demonstrates the application of logistic regression to predict diabetes based on health indicators. The model developed provides a reliable means of predicting diabetes, contributing to early detection and better management of the condition. By analyzing the dataset and training the model, we have shown how diagnostic measurements such as glucose levels, BMI, and age can be used effectively to assess the likelihood of diabetes in female patients of Pima Indian heritage aged 21 and older.

The next steps could involve further refining the model, exploring additional algorithms for comparison, and potentially integrating real-time data to enhance prediction accuracy and reliability. Overall, this project highlights the importance of data-driven approaches in healthcare for improving patient outcomes and facilitating proactive medical interventions.
