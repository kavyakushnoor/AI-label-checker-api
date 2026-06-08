# AI Label Checker API

AI-powered beverage label validation API that uses OCR and rule-based validation to analyze product labels for compliance and completeness.

## Overview

This project provides a REST API for extracting text from beverage label images and validating the extracted information against predefined business or compliance rules.

Core workflow:

1. Upload beverage label image
2. Extract text using Google Cloud Vision OCR
3. Process and structure extracted content
4. Validate against label rules
5. Return validation results and issues

---

## Features

* OCR-powered label text extraction
* Rule-based beverage label validation
* FastAPI REST API
* Google Cloud Vision integration
* Docker support
* Multipart image uploads
* Modular architecture for extensibility

---

## Project Structure

```text
.
├── app.py                  # API entrypoint
├── main.py                 # Application startup / routing
├── extractor.py            # OCR extraction logic
├── validator.py            # Validation engine
├── vision_client.py        # Google Vision client wrapper
├── load.py                 # Data/rule loading utilities
├── credentials/           # Cloud credentials (do not commit secrets)
├── test.py                # Testing utilities
├── requirements.txt
├── Dockerfile
```

---

## Architecture

```text
Image Upload
     │
     ▼
FastAPI Endpoint
     │
     ▼
OCR Extraction Layer
(Google Vision API)
     │
     ▼
Text Processing
     │
     ▼
Validation Engine
(Rules-based checks)
     │
     ▼
Compliance Results API
```

---

## Tech Stack

* FastAPI
* Google Cloud Vision API
* Python
* Pillow
* Uvicorn
* Docker

---

## Installation

### Clone Repository

```bash
git clone <repo-url>
cd AI-label-checker-api
```

### Create Virtual Environment

```bash
python -m venv .vision-ai
source .vision-ai/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```env
GOOGLE_APPLICATION_CREDENTIALS=credentials/service-account.json
```

Place your Google Cloud service account credentials inside:

```text
credentials/
```

---

## Run Locally

```bash
uvicorn app:app --reload
```

API available at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Example API Usage

### Upload Label Image

```bash
curl -X POST \
-F "file=@label.jpg" \
http://localhost:8000/validate
```

### Example Response

```json
{
  "status": "PASS",
  "issues": [],
  "detected_fields": {
      "brand": "Example Beverage",
      "ingredients": true,
      "volume": "12 oz"
  }
}
```

---

## Docker Usage

Build image:

```bash
docker build -t ai-label-checker .
```

Run container:

```bash
docker run -p 8000:8000 ai-label-checker
```

---

## Validation Workflow

1. Receive image upload
2. Preprocess image
3. Send image to Google Vision OCR
4. Extract text blocks
5. Compare extracted text against rules
6. Return validation report

---

## Future Improvements

* Confidence scoring
* Async OCR pipeline
* More validation rules
* Structured field extraction
* User Authentication layer
* Export results to csv
* Historical analysis tracking

---

## Notes

* Google Vision API billing may apply

---

## License

MIT License
