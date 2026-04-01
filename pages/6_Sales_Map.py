import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Map")

df = pd.read_csv("data/superstore.csv")

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Sales by Region"
)

st.plotly_chart(fig, use_container_width=True)