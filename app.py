from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load(r"Fish_dataset.pkl")  
encoder = joblib.load("label_encoder.pkl")  # Load label encoder

@app.route("/")
def home():
    return render_template("input.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect all 6 features
        feature_names = ["Weight", "Length1", "Length2", "Length3", "Height", "Width"]
        features = [float(request.form[key]) for key in feature_names]
        features = np.array(features).reshape(1, -1)

        # Predict numeric label
        predicted_label = model.predict(features)[0]

        # Convert label back to fish species name
        predicted_species = encoder.inverse_transform([predicted_label])[0]

        return render_template("result.html", prediction=predicted_species)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)