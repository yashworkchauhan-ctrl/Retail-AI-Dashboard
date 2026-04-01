import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("AI Customer Segmentation")

# Load dataset
df = pd.read_csv("data/superstore.csv")

# Feature selection
X = df[["Sales", "Profit"]]

# Train KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

st.write("Customer Groups based on Sales & Profit")

# Plot clusters
fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Cluster",
    title="Customer Segments"
)

st.plotly_chart(fig, use_container_width=True)