# Email Spam/Ham Detection

A lightweight machine learning web application that classifies email text as spam or ham (not spam) using a trained natural language processing (NLP) model. The project uses a Flask backend, a TF-IDF vectorizer, and a serialized classification model to analyze incoming email content in real time.

## Overview

This project is designed to detect suspicious and unsolicited email content by examining the text and classifying it based on patterns commonly found in spam messages. It is useful for:

- email filtering
- phishing detection prototypes
- spam classification experiments
- NLP and ML learning projects

The app accepts raw email text through a web form, processes it using a trained model, and returns a prediction result.

## Features

- Text-based spam detection for email content
- Ham vs spam classification using a trained ML model
- Simple and intuitive web interface
- Fast inference through a Flask REST API
- Model-based prediction using TF-IDF text vectorization

## Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn
- Pickle (for loading the ML model and vectorizer)

### Frontend
- HTML5
- Tailwind CSS
- JavaScript
- Jinja2 templates

### Machine Learning
- TF-IDF vectorizer for text transformation
- Pre-trained spam classification model stored as `email_model.pkl`
- Text preprocessing and feature extraction using saved transformer model `transform_model.pkl`

## Project Structure

```text
Email-Spam-Ham-Detection/
├── app.py                  # Flask app and email prediction API
├── email_model.pkl        # Trained spam classification model
├── transform_model.pkl     # TF-IDF vectorizer used for text feature extraction
├── requirements.txt        # Python dependencies
├── templates/
│   └── email.html          # Frontend interface
├── readme.md              # Project documentation
└── .gitignore             # Optional git ignore settings (if present)
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Email-Spam-Ham-Detection
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask server:

```bash
python app.py
```

Then open the app in your browser at:

```text
http://127.0.0.1:5000/
```

## API Endpoint

The project exposes a prediction endpoint:

```http
POST /api/diabetes
```

Although the route name is `diabetes`, the app is actually used for email spam detection and expects email text as input.

Example JSON payload:

```json
{
  "email": "Congratulations! You have won a free cash prize. Click here to claim your reward now!"
}
```

Example response:

```json
{
  "predicion": 1,
  "confidence": 97
}
```

### Response Meaning

- `predicion` / `prediction`: result of the classifier
- `1` typically indicates spam
- `0` typically indicates ham

## Notes

- The app loads the trained vectorizer from `transform_model.pkl` and the model from `email_model.pkl` at runtime.
- This project is suitable for learning and demonstration purposes.
- For production use, you would typically add input validation, improved preprocessing, model evaluation, and deployment security measures.

## License

This project is intended for educational and demonstration purposes. Add a license file if you plan to distribute or deploy it publicly.
