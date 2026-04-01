import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/superstore.csv")

X = df[['Discount']]
y = df['Sales']

model = RandomForestRegressor()

model.fit(X,y)

st.success("Model Trained Successfully")