import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Product Analysis")

df = pd.read_csv("data/superstore.csv")

# -----------------------------
# TOP PRODUCTS
# -----------------------------

st.subheader("Top 10 Selling Products")

top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

fig = px.bar(
    top_products,
    title="Top Selling Products",
    labels={"value":"Sales","Sub-Category":"Product"}
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# CATEGORY PERFORMANCE
# -----------------------------

st.subheader("Category Performance")

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# PRODUCT PROFIT
# -----------------------------

st.subheader("Product Profitability")

profit_products = df.groupby("Sub-Category")["Profit"].sum().reset_index()

fig3 = px.bar(
    profit_products,
    x="Sub-Category",
    y="Profit",
    color="Profit"
)

st.plotly_chart(fig3, use_container_width=True)