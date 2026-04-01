import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.title("AI Demand Forecasting")

# -----------------------
# LOAD DATA
# -----------------------

df = pd.read_csv("data/superstore.csv")

# -----------------------
# FIND DATE COLUMN
# -----------------------

date_column = None

for col in df.columns:
    if "date" in col.lower():
        date_column = col
        break

if date_column is None:
    st.error("No date column found in dataset")
    st.stop()

# -----------------------
# PREPARE DATA
# -----------------------

df[date_column] = pd.to_datetime(df[date_column])

sales_data = df.groupby(date_column)["Sales"].sum().reset_index()

sales_data = sales_data.sort_values(date_column)

sales_data["Day"] = np.arange(len(sales_data))

X = sales_data[["Day"]]
y = sales_data["Sales"]

# -----------------------
# TRAIN MODEL
# -----------------------

model = LinearRegression()
model.fit(X, y)

# -----------------------
# FORECAST DAYS
# -----------------------

future_days = st.slider("Select Future Days", 1, 30, 7)

future_X = np.arange(len(sales_data), len(sales_data)+future_days).reshape(-1,1)

predictions = model.predict(future_X)

forecast_df = pd.DataFrame({
    "Day":future_X.flatten(),
    "Predicted Sales":predictions
})

# -----------------------
# HISTORICAL SALES
# -----------------------

st.subheader("Historical Sales")

fig1 = px.line(
    sales_data,
    x=date_column,
    y="Sales",
    title="Past Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# FORECAST SALES
# -----------------------

st.subheader("Future Sales Forecast")

fig2 = px.line(
    forecast_df,
    x="Day",
    y="Predicted Sales",
    title="Forecasted Sales"
)

st.plotly_chart(fig2, use_container_width=True)