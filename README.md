<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manufacturing Operations API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            text-align: center;
        }
        ul {
            margin-left: 20px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        .section {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Manufacturing Operations API</h1>

    <div class="section">
        <h2>Overview</h2>
        <p>This project is a RESTful API designed for predictive analysis of manufacturing operations. It allows users to:</p>
        <ul>
            <li>Upload a dataset of machine operations.</li>
            <li>Train a machine learning model to predict machine downtime.</li>
            <li>Make predictions based on input features like temperature and runtime.</li>
        </ul>
        <p>The API is built using <strong>Flask</strong> and <strong>scikit-learn</strong>.</p>
    </div>

    <div class="section">
        <h2>Features</h2>
        <ol>
            <li><strong>Upload Endpoint (POST /upload):</strong>
                <ul>
                    <li>Accepts a CSV file containing manufacturing data.</li>
                    <li>Saves the file on the server for further processing.</li>
                </ul>
            </li>
            <li><strong>Train Endpoint (POST /train):</strong>
                <ul>
                    <li>Trains a Decision Tree Classifier on the uploaded dataset.</li>
                    <li>Returns model performance metrics, including accuracy and a classification report.</li>
                </ul>
            </li>
            <li><strong>Predict Endpoint (POST /predict):</strong>
                <ul>
                    <li>Accepts JSON input with features (<code>Temperature</code>, <code>Run_Time</code>).</li>
                    <li>Returns predictions for downtime (<code>Yes</code>/<code>No</code>) along with confidence scores.</li>
                </ul>
            </li>
        </ol>
    </div>

    <div class="section">
        <h2>Technologies Used</h2>
        <ul>
            <li><strong>Python:</strong> Programming language for the API.</li>
            <li><strong>Flask:</strong> Framework for building the RESTful API.</li>
            <li><strong>scikit-learn:</strong> Library for machine learning model development.</li>
            <li><strong>pandas:</strong> Data processing and manipulation.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Usage Instructions</h2>
        <h3>1. Upload Dataset (POST /upload)</h3>
        <p><strong>Request:</strong> Use a tool like Postman or cURL to send a file.</p>
        <pre><code>
curl -X POST http://127.0.0.1:5000/upload \
-F "file=@/path/to/your/dataset.csv"
        </code></pre>
        <p><strong>Response:</strong></p>
        <pre><code>
{
    "message": "File uploaded successfully",
    "file_path": "data/dataset.csv"
}
        </code></pre>

        <h3>2. Train the Model (POST /train)</h3>
        <p><strong>Request:</strong> Simply send a POST request to the endpoint.</p>
        <pre><code>
curl -X POST http://127.0.0.1:5000/train
        </code></pre>
        <p><strong>Response:</strong> Example output:</p>
        <pre><code>
{
    "message": "Model trained successfully",
    "accuracy": 0.85,
    "classification_report": { ... }
}
        </code></pre>

        <h3>3. Make Predictions (POST /predict)</h3>
        <p><strong>Request:</strong> Send a JSON payload with the input features:</p>
        <pre><code>
{
    "Temperature": 85.0,
    "Run_Time": 120
}
        </code></pre>
        <pre><code>
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"Temperature": 85.0, "Run_Time": 120}'
        </code></pre>
        <p><strong>Response:</strong></p>
        <pre><code>
{
    "Downtime": "Yes",
    "Confidence": 0.85
}
        </code></pre>
    </div>

    <div class="section">
        <h2>Project Structure</h2>
        <pre><code>
project_directory/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── data/                # Directory for uploaded datasets
├── models/              # Directory for saving trained models
└── README.html          # Project documentation
        </code></pre>
    </div>

    <div class="section">
        <h2>Future Enhancements</h2>
        <ul>
            <li>Improve Model Performance:</li>
            <ul>
                <li>Use advanced models like Random Forest or Gradient Boosting.</li>
                <li>Address class imbalance in the dataset.</li>
            </ul>
            <li>Add Deployment:</li>
            <ul>
                <li>Deploy the API to a cloud platform (e.g., Heroku, AWS).</li>
            </ul>
            <li>Extend Features:</li>
            <ul>
                <li>Add more input features like machine age or maintenance history.</li>
            </ul>
        </ul>
    </div>

    <div class="section">
        <h2>Contact</h2>
        <p>For any questions or issues, please reach out to:</p>
        <p><strong>Email:</strong> <a href="mailto:adityaraj6043@gmail.com">adityaraj6043@gmail.com</a></p>
        <p><strong>Phone:</strong> +91 7322057950</p>
    </div>
</body>
</html>
