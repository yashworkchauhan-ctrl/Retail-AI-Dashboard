import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# dataset load
df = pd.read_csv("data/superstore.csv")

# clean column names
df.columns = df.columns.str.strip()

print("Dataset loaded successfully")

# features
X = df[['Quantity','Discount']]

# target
y = df['Sales']

# train test split
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# model create
model = RandomForestRegressor()

# train model
model.fit(X_train,y_train)

# prediction
predictions = model.predict(X_test)

# error calculate
error = mean_absolute_error(y_test,predictions)

print("Model MAE:", error)

# save model
pickle.dump(model, open("models/model.pkl","wb"))

print("Model saved successfully!")