import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Profit Analysis")

df = pd.read_csv("data/superstore.csv")

# -----------------------------
# DISCOUNT VS PROFIT
# -----------------------------

st.subheader("Discount vs Profit")

fig = px.scatter(
    df,
    x="Discount",
    y="Profit",
    color="Category"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# PROFIT BY REGION
# -----------------------------

st.subheader("Profit by Region")

profit_region = df.groupby("Region")["Profit"].sum().reset_index()

fig2 = px.bar(
    profit_region,
    x="Region",
    y="Profit",
    color="Region"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# LOSS PRODUCTS
# -----------------------------

st.subheader("Loss Making Products")

loss_products = df[df["Profit"] < 0]

fig3 = px.histogram(
    loss_products,
    x="Sub-Category",
    color="Sub-Category"
)

st.plotly_chart(fig3, use_container_width=True)