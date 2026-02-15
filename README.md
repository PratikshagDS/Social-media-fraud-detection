Machine learning project to detect fake social media accounts
Social Media Fraud Detection System

1.Project Overview
This project is a Machine Learning based system to detect fake and fraudulent social media accounts.
It analyzes user profile and activity features to classify accounts as Real or Fake.

2.Problem Statement
Fake social media accounts are widely used for spam, scams, and misinformation. Manual detection is time-consuming and unreliable.
This project automates the detection process using Machine Learning models.

3.Models Used
XGBoost (for Instagram and Twitter)
Random Forest (for Facebook and LinkedIn)

4.Dataset
The dataset contains features such as:
followers_count
following_count
posts_count
account_age
has_profile_pic
bio_length
username_length
is_verified
label (0 = Real, 1 = Fake)

5.Technologies Used
Python
Pandas, NumPy
Scikit-learn
XGBoost
Streamlit (for frontend)

6.Project Workflow
Data collection
Data cleaning and preprocessing
Exploratory Data Analysis (EDA)
Feature engineering
Train-test split
Model training
Model evaluation
Model saving (.pkl files)
Frontend integration using Streamlit

7. Results
Instagram Model Accuracy:99.9%
Twitter Model Accuracy:99.9 %
Facebook Model Accuracy: 100%
LinkedIn Model Accuracy: 100%

8.How to Run the Project
Clone the repository
Install required libraries:
pip install -r requirements.txt
Run the application:
streamlit run app.py

9.Project Structure
social-media-fraud-detection/
├── README.md
├── app.py
├── models/
├── data/
├── notebooks/
└── requirements.txt
10. Author
Pratiksha Gavhale.
