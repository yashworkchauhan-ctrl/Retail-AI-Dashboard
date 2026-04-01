import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("data/superstore.csv")

# clean column names
df.columns = df.columns.str.strip()

print("Columns in dataset:")
print(df.columns)

# -------------------------------
# SALES BY REGION
# -------------------------------

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=region_sales, x="Region", y="Sales")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# -------------------------------
# SALES BY CATEGORY
# -------------------------------

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=category_sales, x="Category", y="Sales")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()