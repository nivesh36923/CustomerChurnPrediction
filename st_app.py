import streamlit as st
import pandas as pd 
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
import joblib

st.title('Customer Churn Predictor')

st.write('**fil the data**')


loaded_model = xgb.XGBClassifier()
loaded_model.load_model("xgb_model_save.json")


Account_length = st.number_input("**Account length:**", value=3.452)
Area_code = st.number_input("**Area code**", value=3.452)
Total_day_minutes = st.number_input("**Total day minutes:**", value=3.452)
Total_day_calls = st.number_input("**Total day calls:**", value=3.452)
Total_day_charge = st.number_input("**Total day charge:**", value=3.452)
Total_eve_minutes = st.number_input("**Total eve minutes:**", value=3.452)
Total_eve_calls = st.number_input("**Total eve calls:**", value=3.452)
Total_eve_charge = st.number_input("**Total eve charge:**", value=3.452)
Total_night_minutes = st.number_input("**Total night minutes:**", value=3.452)
Total_night_calls = st.number_input("**Total night calls:**", value=3.452)
Total_night_charge = st.number_input("**Total night charge:**", value=3.452)
Customer_service_calls = st.number_input("**Customer service calls:**", value=3.452)
agree = st.checkbox('Tick')
if agree == True:
  st.write('welcome')



  if st.button("Submit"):
    X = np.array([Account_length,Area_code,Total_day_minutes,Total_day_calls,Total_day_charge,Total_eve_minutes,Total_eve_calls,Total_eve_charge,Total_night_minutes,Total_night_calls,Total_night_charge,Customer_service_calls])
    X_test = X.reshape(1, -1)
    y_pred = loaded_model.predict(X_test)
    
    st.write('y_pred : ',y_pred)
    


