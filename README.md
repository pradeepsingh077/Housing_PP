# 🏡 Housing Price Prediction App – Full Stack ML Deployment

Welcome to the **Housing_PP** project – a full-stack application that combines machine learning, data preprocessing, and API integration to predict **house prices** based on user input. This project is built using **Flask**, **XGBoost**, and **Pandas**, with optional visual exploration in Jupyter Notebooks and Power BI dashboards.

---

## 📌 Table of Contents

- [Project Summary](#project-summary)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [API Endpoints](#api-endpoints)
- [Prediction Example](#prediction-example)
- [Directory Structure](#directory-structure)
- [Demo Screenshots](#demo-screenshots)
- [Data Overview](#data-overview)
- [Model Details](#model-details)
- [Notebook Insights](#notebook-insights)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📘 Project Summary

This project provides an ML-powered solution for **predicting house prices** based on features such as city, number of bedrooms, square footage, floor level, area type, bathroom count, and furnishing status. The trained model is served via **REST APIs** using **Flask**, enabling seamless integration with front-end applications or automated systems.

The goal is to simulate a production-grade environment for deploying and interacting with a regression model, ideal for demonstrating full-cycle ML operations.

---

## 🚀 Key Features

✅ Cleaned and processed real estate dataset  
✅ XGBoost regression model training and evaluation  
✅ RESTful APIs via Flask for integration  
✅ Prediction through both form input and JSON API  
✅ Reusable code with modular scripts  
✅ Power BI or Notebook-based data exploration  
✅ Model saved as `.pkl` for deployment  
✅ Python script to test API using `requests`

---

## 🛠️ Tech Stack

| Component        | Tech Used                   |
|------------------|-----------------------------|
| Backend          | Python, Flask               |
| ML Model         | XGBoost, scikit-learn       |
| Data Handling    | Pandas, NumPy               |
| Visualization    | Matplotlib, Seaborn         |
| API Testing      | `requests` library          |
| Deployment       | Localhost via Flask server  |
| Dataset Format   | CSV                         |

---

## 🧩 Project Architecture

                    ┌────────────┐
                    │  Dataset   │
                    └────┬───────┘
                         ↓
            ┌────────────────────┐
            │  Preprocessing     │ ← clean_data.csv
            └────────────────────┘
                         ↓
            ┌────────────────────┐
            │  XGBoost Training  │ ← XGBoostingModel.pkl
            └────────────────────┘
                         ↓
               ┌──────────────────┐
               │  Flask API App   │ ← app.py / server.py
               └──────────────────┘
                         ↓
       ┌──────────────────────────────┐
       │  Client Request via request.py │
       └──────────────────────────────┘

---

## 🧪 Setup Instructions

### 📦 Install Requirements

```bash
# Clone the repository
git clone https://github.com/pradeepsingh077/Housing_PP.git
cd Housing_PP
```
# Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

# Install dependencies
```bash
pip install -r Requirement.txt
```
# ⚙️ How It Works
The model is trained and saved as XGBoostingModel.pkl.

The Flask app reads clean_data.csv and loads the model.

Two endpoints are available:

/predict: accepts HTML form-style POST requests.

/predict_api: accepts raw JSON POST data.

Incoming request data is transformed into a Pandas DataFrame.

Model makes a prediction and returns the result (price in lakhs).

# 🌐 API Endpoints
1. POST /predict
Form-data input (ideal for HTML forms or tools like Postman):

City, BHK, Size, Floor, AreaType, FurnishingStatus, Bathroom

Returns: String-form prediction

2. POST /predict_api
JSON input (ideal for programmatic use)

{
  "City": "Bangalore",
  "BHK": 2,
  "Size": 1200,
  "Floor": 5,
  "AreaType": "Super built-up",
  "FurnishingStatus": "Semi-furnished",
  "Bathroom": 2
}

# 📤 Prediction Example
Use the request.py script to test the API:

python request.py
# 🗂️ Directory Structure

Housing_PP/
│
├── clean_data.csv              # Preprocessed dataset
├── XGBoostingModel.pkl         # Trained model
├── Requirement.txt             # Python dependencies
│
├── app.py                      # Flask backend with /predict and /predict_api
├── server.py                   # Alternative Flask API route
├── request.py                  # API testing script
├── Housing.ipynb               # Jupyter notebook with data EDA
└── README.md                   # Project documentation

# 🧠 Data Overview
The dataset contains the following features:

Feature	Description
City	City where property is located
BHK	Number of bedrooms
Size	Total square feet
Floor	Which floor the house is on
AreaType	Super built-up, built-up, etc.
FurnishingStatus	Furnished, Semi-furnished, Unfurnished
Bathroom	Number of bathrooms
Price	Target variable (in lakhs)

# 🤖 Model Details
Model used: XGBoost Regressor

Training Data: Cleaned version of housing dataset

Input Shape: 7 features

Output: Continuous numeric value (Price in lakhs)

Saving: Trained model serialized using pickle

Advantages of XGBoost:

Handles missing values well

High performance for tabular data

Supports feature importance and tuning

# 📓 Notebook Insights (Housing.ipynb)
The notebook includes:

Exploratory data analysis using Seaborn & Matplotlib

Feature correlation analysis

Preprocessing: handling missing values, encoding categoricals

Train/test split & model evaluation

Visualizations of actual vs predicted prices

Recommended to run in Jupyter for visual insights.

# 🤝 Contributing
Contributions are welcome!

To contribute:
Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Make your changes

Push and open a Pull Request

Make sure to format code with proper linting and add docstrings where necessary.

# 📜 License
This project is licensed under the MIT License.

See the LICENSE.md file for full license text.

# 📬 Contact
Author: Pradeep Singh

📧 Email: pradeepsingh.psk610@gmail.com

🌐 LinkedIn: linkedin.com/in/pradeep-singh-585931230

