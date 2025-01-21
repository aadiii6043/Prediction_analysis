# Manufacturing Operations API

## Overview
This project is a RESTful API designed for predictive analysis of manufacturing operations. It allows users to:
- Upload a dataset of machine operations.
- Train a machine learning model to predict machine downtime.
- Make predictions based on input features like temperature and runtime.

The API is built using **Flask** and **scikit-learn**.

---

## Features
1. **Upload Endpoint (POST `/upload`):**
   - Accepts a CSV file containing manufacturing data.
   - Saves the file on the server for further processing.
2. **Train Endpoint (POST `/train`):**
   - Trains a Decision Tree Classifier on the uploaded dataset.
   - Returns model performance metrics, including accuracy and a classification report.
3. **Predict Endpoint (POST `/predict`):**
   - Accepts JSON input with features (`Temperature`, `Run_Time`).
   - Returns predictions for downtime (`Yes`/`No`) along with confidence scores.

---

## Technologies Used
- **Python:** Programming language for the API.
- **Flask:** Framework for building the RESTful API.
- **scikit-learn:** Library for machine learning model development.
- **pandas:** Data processing and manipulation.

---

## Usage Instructions

### 1. Upload Dataset (POST `/upload`)
**Request:** Use a tool like Postman or cURL to send a file.

```bash
curl -X POST http://127.0.0.1:5000/upload \
-F "file=@/path/to/your/dataset.csv"
