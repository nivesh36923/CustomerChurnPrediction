import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report


st.title('Customer Churn Prediction')
st.write('Hello world!')


df_20 = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/CustomerChurnPrediction/master/churn-bigml-20.csv')
df_80 = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/CustomerChurnPrediction/master/churn-bigml-80.csv')

df = pd.concat([df_20,df_80])
le = LabelEncoder()
df = df.reset_index()

with st.expander('Data'):
  df
df['State'] = le.fit_transform(df['State'])


with st.expander('Data'):
  df
