import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("AI Sales Prediction")

# Dataset load
df = pd.read_csv("data/superstore.csv")

# Model training
X = df[["Quantity", "Discount"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

# User input
quantity = st.number_input("Enter Quantity", 1, 100, 10)
discount = st.number_input("Enter Discount", 0.0, 1.0, 0.50)

# Prediction button
if st.button("Predict Sales"):

    input_data = [[quantity, discount]]

    prediction = model.predict(input_data)

    # Save prediction in session
    st.session_state["predicted_sales"] = prediction[0]

    st.success(f"Predicted Sales: {prediction[0]:.2f}")