import streamlit as st
import pandas as pd
st.title('Customer Churn Prediction')

st.write('Hello world!')

df = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/CustomerChurnPrediction/master/Churn-bigml-20.csv')

with st.expander('Data'):
  df
