import streamlit as st
import pandas as pd
st.title('Customer Churn Prediction')

st.write('Hello world!')

df = pd.read_csv('https://raw.githubusercontent.com/nivesh36923/nd-ml/master/stock_data.csv')

with st.expander('Data'):
  df
