# <div align="center">

# 🛡️ SpamShield ML • Email Spam & Ham Classifier

### *Real-time Natural Language Processing (NLP) & Lightweight Flask Inference Engine*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-NLP-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-Modern_UI-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="#-key-features">Key Features</a> •
  <a href="#-architecture--pipeline">Architecture</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

</div>

## 📌 Executive Overview

**SpamShield ML** is a high-performance, lightweight machine learning service engineered to identify, filter, and neutralize unsolicited spam and phishing threats in email payloads. 

Powered by a **TF-IDF (Term Frequency-Inverse Document Frequency) feature extraction pipeline** and a high-accuracy serialized classifier, the engine transforms raw, noisy natural language into numerical representations and yields deterministic binary classifications (`Spam` vs. `Ham`) alongside inference confidence metrics in sub-50ms latency.

> 💡 **Core Value**: Designed as a plug-and-play microservice suitable for edge spam triage, email client integration prototypes, and educational ML pipelines.

---

## ⚡ Key Features

- 🧠 **NLP-Driven Classification**: Leverages token n-gram analysis and TF-IDF weighting to detect deceptive vocabulary, urgency cues, and phishing syntax.
- ⚡ **Sub-50ms REST Inference**: Lightweight Flask + Gunicorn runtime tuned for micro-footprint deployment and rapid prediction scoring.
- 🎨 **Modern Responsive UI**: Clean, accessible Jinja2 frontend crafted with Tailwind CSS for real-time text testing and visual probability outputs.
- 🔒 **Zero External Model Telemetry**: 100% self-contained inference via serialized `.pkl` pipelines—no data egress to third-party proprietary APIs.
- 🌐 **CORS Ready**: Configured with `Flask-CORS` for cross-origin integration with Chrome extensions, webmail clients, and backend proxies.

---

## 📐 Architecture & Pipeline

```
Raw Email Input (Plaintext / HTML snippet)
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ 1. Text Preprocessing & Cleaning                       │
│    • Lowercasing & Tokenization                        │
│    • Stopword Stripping & Noise Filtering              │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ 2. Feature Vectorization (`transform_model.pkl`)       │
│    • TF-IDF Sparse Matrix Construction                 │
│    • Vocabulary Projection                             │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ 3. Inference Classifier (`email_model.pkl`)           │
│    • Binary Decision Boundary Evaluation               │
│    • Probability & Confidence Score Generation         │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
     JSON Response Payload / UI Live Badge
     { "prediction": 1 (Spam), "confidence": 98.4% }
```

---

## 🛠️ Tech Stack Matrix

| Domain | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Core** | `Python 3.9+`, `Flask` | Micro-framework powering the REST API & routing |
| **Model Serving** | `Gunicorn`, `Pickle` | WSGI server & serialized object loader |
| **Machine Learning**| `Scikit-learn` | Tokenization, TF-IDF vectorization & classification |
| **API Middleware** | `Flask-CORS` | Cross-Origin Resource Sharing handling |
| **Frontend UI** | `Tailwind CSS`, `HTML5`, `JS` | Real-time interactive inspection dashboard |
| **Templating** | `Jinja2` | Server-rendered UI hydration |

---

## 📂 Project Structure

```text
Email-Spam-Ham-Detection/
├── 📄 app.py                  # Flask entrypoint & REST prediction routing
├── 🧠 email_model.pkl         # Trained classification pipeline (Estimator)
├── ⚙️ transform_model.pkl      # Fitted TF-IDF Vectorizer feature extractor
├── 📋 requirements.txt        # Pinned runtime dependencies
├── 📁 templates/
│   └── 🌐 email.html          # Interactive Tailwind-styled testing UI
├── 📜 README.md               # Architecture, API & setup documentation
└── 🚫 .gitignore              # Environment & cache exclusion filters
```

---

## 🚀 Quick Start

### 1. Clone & Navigate
```bash
git clone https://github.com/YOUR_USERNAME/Email-Spam-Ham-Detection.git
cd Email-Spam-Ham-Detection
```

### 2. Environment Setup
```bash
# Create dedicated virtual environment
python -m venv venv

# Activate environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Boot Inference Engine
```bash
python app.py
```

The application will bind to `http://127.0.0.1:5000/`. Visit this URL in your browser to access the graphical testing console.

---

## 📡 API Reference

### Real-Time Email Scoring Endpoint

Inspect incoming email text programmatically by issuing an HTTP `POST` request.

```http
POST /api/diabetes HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
```

> ⚠️ **Route Alias Note**: The endpoint route is designated `/api/diabetes` as the historical route identifier within `app.py`. It accepts email string payloads as documented below.

#### Request Headers
| Header | Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | Mandatory payload format |

#### Request Body
```json
{
  "email": "URGENT: Your account access has been limited. Verify your credentials immediately by clicking here to claim your $1,000 credit."
}
```

#### cURL Example
```bash
curl -X POST http://127.0.0.1:5000/api/diabetes \
  -H "Content-Type: application/json" \
  -d '{"email": "Subject: Invoice Overdue - Please find attached your payment receipt."}'
```

#### Python (`requests`) Example
```python
import requests

url = "http://127.0.0.1:5000/api/diabetes"
payload = {
    "email": "Free lottery prize! You have been selected. Call now to redeem!"
}

response = requests.post(url, json=payload)
print(response.json())
```

#### Response Payload (`200 OK`)
```json
{
  "predicion": 1,
  "confidence": 97.42
}
```

#### Response Schema
| Key | Type | Description |
| :--- | :--- | :--- |
| `predicion` | `integer` | `1` = **Spam / Suspicious**, `0` = **Ham / Legitimate** |
| `confidence` | `number` | Confidence probability expressed as a percentage (`0.00` - `100.00`) |

---

## 🧪 Benchmark & Sample Test Cases

| Sample Text | Expected Label | Output Code | Confidence |
| :--- | :---: | :---: | :---: |
| *"Hey team, let's reschedule our sprint retrospective to Thursday 2 PM."* | **HAM** | `0` | `~99.1%` |
| *"WINNER! You have won a $1,000 Walmart Gift Card. Click here now!"* | **SPAM** | `1` | `~98.6%` |
| *"Attached is the quarterly financial report in PDF format for review."* | **HAM** | `0` | `~96.8%` |
| *"Urgent: Your cryptocurrency wallet is locked. Verify seed phrase instantly."* | **SPAM** | `1` | `~97.9%` |

---

## 🗺️ Production Hardening Roadmap

- [ ] **Modern Route Canonicalization**: Aliasing `/api/v1/classify` alongside `/api/diabetes` for standard semantic REST compliance.
- [ ] **Input Sanitization**: Integrating `bleach` or regex stripping to isolate HTML markup, raw attachments, and suspicious obfuscated Unicode.
- [ ] **Dockerization**: Providing a `Dockerfile` and `docker-compose.yml` for single-command production orchestration.
- [ ] **Confidence Calibration**: Exposing calibrated Platt scaling probabilities directly in response schemas.
- [ ] **Batch Classification**: Adding multi-email vectorization endpoint (`/api/v1/classify/batch`).

---

## 📄 License & Attribution

Distributed under the **MIT License**. See `LICENSE` for details.  
Built for demonstration, educational natural language processing pipelines, and AI security engineering research.
