# Fish_Market_Prediction

#  Fish Market Prediction (ML Model Deployment with Flask)

##  Project Overview

This project is a **Machine Learning (ML) model deployment** that predicts the **species of a fish** based on its measurements. The model is trained using the **Fish Market dataset** and deployed locally using **Flask**.

##  Project Structure

Fish_Market_Prediction/
├── Fish_Market_ML_Model.ipynb  # saved python model(MODEL TRAINING)
├── Fish_dataset.pkl            # Saved ML Model
├── label_encoder.pkl           # Label Encoding File
├── app.py                      # Flask API (Backend)
├── templates/
│   ├── input.html              # Input Form (Frontend)
│   ├── result.html             # Prediction Output Page
├── Fish.csv                    # Dataset (Fish Market Data)
├── README.md                   # Project Documentation


##  Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/Fish_Market_Prediction.git
cd Fish_Market_Prediction
```

###  Install Dependencies

pip install flask pandas numpy scikit-learn joblib

###  Run Flask API Locally

python app.py

 The API will be available at:\
http://127.0.0.1:5000/(http://127.0.0.1:5000/)

## Usage Guide

### 1. Web-Based Prediction

- Open [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/) in a web browser.
- Enter fish measurements (**Length, Height, Width**).
- Click **Predict** to see the estimated **species**.

###  2. API Testing with Postman or cURL

Send a **POST request** to `http://127.0.0.1:5000/predict` with the following JSON data:

```json
{
    "Length1": 23.2,
    "Length2": 25.4,
    "Length3": 30.0,
    "Height": 11.52,
    "Width": 4.02,
    "Weight": 20,
}
```

Response Example:

```json
{"prediction": "Perch"}
```

##  Machine Learning Model

- **Dataset**: [Fish Market Dataset (Kaggle)](https://www.kaggle.com/aungpyaeap/fish-market)
- **Problem Type**: Classification (Predicting fish species)
- **Algorithm Used**: **Random Forest / SVM**
- **Features Used**:
  - `Length1` (Vertical Length)
  - `Length2` (Diagonal Length)
  - `Length3` (Cross Length)
  - `Height`
  - `Width`
  - weight

## ScreenshotS

| Description                       Screenshot 
 --------------------------------------  ---------- 
Flask API Running                   Included 
Frontend Page                       Included 
Terminal Logs (API Requests)        Included 
Prediction Results (Web & Postman)  Included 
GitHub Repository                   Included 


##  Contribution & Author
Feel free to contribute! Fork the repository, create an issue, or submit a **Pull Request**.

 GitHub Repository: [Your GitHub Repo Link Here](https://github.com/varsha-reghu/Fish_Market_Prediction)

 Author: Varsha Reghu 
 Date: 16TH March 2025  


