import streamlit as st
import pandas as pd 
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
import joblib

st.title('Customer Churn Prediction')
st.write('Hello world!')


df_20 = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/CustomerChurnPrediction/master/churn-bigml-20.csv')
df_80 = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/CustomerChurnPrediction/master/churn-bigml-80.csv')

df = pd.concat([df_20,df_80])
dfcopy = df.copy()
le = LabelEncoder()
df = df.reset_index()

with st.expander('Data'):
  df
df['State'] = le.fit_transform(df['State'])


X = df[[
    'Account length','Area code','Total day minutes','Total day calls', 'Total day charge',
    'Total eve minutes','Total eve calls', 'Total eve charge', 'Total night minutes',
    'Total night calls', 'Total night charge', 'Customer service calls'
]]

y = df['Churn']
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2)

from xgboost import XGBClassifier


xgb_clf = XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    use_label_encoder=False
)


xgb_clf.fit(X_train, y_train)
st.info('process done')


st.selectbox('**Select State**',dfcopy['State'])
Account_length = st.number_input("**Account length:**", value=3.452)
Area_code = st.number_input("Area code**", value=3.452)
Total_day_minutes = st.number_input("**Total day minutes:**", value=3.452)
Total_day_calls = st.number_input("**Total day calls:**", value=3.452)
Total_day_charge = st.number_input("**Total day charge:**", value=3.452)
Total_eve_minutes = st.number_input("**Total eve minutes:**", value=3.452)
Total_eve_calls = st.number_input("**Total eve calls:**", value=3.452)
Total_eve_charge = st.number_input("**Total eve charge:**", value=3.452)
Total_night_minutes = st.number_input("**Total night minutes:**", value=3.452)
Total_night_calls = st.number_input("**Total night calls:**", value=3.452)
Total_night_charge = st.number_input("**Total night charge:**", value=3.452)
Customer_service_calls = st.number_input("**TCustomer service calls:**", value=3.452)


user_test = {'Account length' : Account_length , 'Area code' : Area_code,
          'Total day minutes' : Total_day_minutes ,'Total day calls' : Total_day_calls , 
             'Total day charge' : Total_day_charge,
        'Total eve minutes' : Total_eve_minutes ,
       'Total eve calls' : Total_eve_calls, 'Total eve charge' : Total_eve_charge , 'Total night minutes' : Total_night_minutes  ,
       'Total night calls' : Total_night_calls, 'Total night charge' : Total_night_charge,
             'Customer service calls' : Customer_service_calls}

y_pred = xgb_clf.predict(user_test)

st.write(y_pred)





