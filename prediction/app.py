from flask import Flask, request, jsonify
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Manufacturing API is running!"})

# Upload endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": f"File {file.filename} uploaded successfully", "file_path": filepath}), 200

# Train endpoint
@app.route('/train', methods=['POST'])
def train_model():
    try:
        # Find the latest file uploaded in the UPLOAD_FOLDER
        uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
        if not uploaded_files:
            return jsonify({"error": "No file found in the upload directory"}), 400
        
        # Assume the most recently uploaded file is the one to use
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_files[-1])
        
        # Load the CSV file
        data = pd.read_csv(file_path)
        
        # Ensure the dataset contains the expected columns
        required_columns = ['Temperature', 'Run_Time', 'Downtime_Flag']
        if not all(column in data.columns for column in required_columns):
            return jsonify({"error": "Dataset does not contain the required columns"}), 400
        
        # Encode the target column (Downtime_Flag: Yes/No -> 1/0)
        data['Downtime_Flag'] = data['Downtime_Flag'].map({'Yes': 1, 'No': 0})
        
        # Define features (X) and target (y)
        X = data[['Temperature', 'Run_Time']]
        y = data['Downtime_Flag']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a Decision Tree Classifier
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Save the trained model
        model_path = os.path.join('models', 'model.pkl')
        os.makedirs('models', exist_ok=True)
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        
        # Return performance metrics
        return jsonify({
            "message": "Model trained successfully",
            "accuracy": accuracy,
            "classification_report": report
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the trained model
        model_path = os.path.join('models', 'model.pkl')
        if not os.path.exists(model_path):
            return jsonify({"error": "No trained model found. Please train the model first."}), 400
        
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # Get the input data from the request
        data = request.get_json()
        if not data or 'Temperature' not in data or 'Run_Time' not in data:
            return jsonify({"error": "Invalid input. Provide 'Temperature' and 'Run_Time'"}), 400
        
        # Extract features for prediction
        temperature = data['Temperature']
        run_time = data['Run_Time']
        input_features = [[temperature, run_time]]
        
        # Make prediction
        prediction = model.predict(input_features)
        confidence = model.predict_proba(input_features).max()
        
        # Return the prediction
        return jsonify({
            "Downtime": "Yes" if prediction[0] == 1 else "No",
            "Confidence": round(confidence, 2)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)