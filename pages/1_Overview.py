import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Overview Dashboard")

# Show latest predicted sale
if "predicted_sales" in st.session_state:
    st.metric("Latest Predicted Sale", round(st.session_state["predicted_sales"], 2))

# Load dataset
df = pd.read_csv("data/superstore.csv")

# Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

# Sales by category chart
st.subheader("Sales by Category")

sales_category = df.groupby("Category")["Sales"].sum().reset_index()

fig = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    color="Category",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)