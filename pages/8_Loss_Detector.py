import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Loss Detection System")

df = pd.read_csv("data/superstore.csv")

loss_df = df[df["Profit"] < 0]

st.subheader("Loss Making Orders")

st.dataframe(loss_df)

fig = px.bar(
    loss_df,
    x="Sub-Category",
    y="Profit",
    color="Sub-Category"
)

st.plotly_chart(fig, use_container_width=True)