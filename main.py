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



