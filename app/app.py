from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load model
model = pickle.load(open("models/model.pkl","rb"))

@app.route("/")
def home():
    return "Retail Sales Prediction API"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    quantity = data["Quantity"]
    discount = data["Discount"]

    prediction = model.predict([[quantity, discount]])

    return jsonify({
        "Predicted Sales": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)