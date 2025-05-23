# FastAPI ASR Application with NVIDIA NeMo (ONNX)

## Overview

This project provides a FastAPI-based web service for automatic speech recognition (ASR) using an ONNX-optimized NVIDIA NeMo model (`stt_hi_conformer_ctc_medium`). The service accepts `.wav` audio files (16kHz, >5 seconds) and returns transcribed text.

---

## Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/projectultra/glowing-octo-waffle.git
cd glowing-octo-waffle
```

### 2. Download Model Files

Place the following files in the `model/` directory:
- `stt_hi_conformer_ctc_medium.onnx`
- `tokens.txt`

### 3. Build the Docker Image

```bash
docker build -t nemo-asr-app .
```

### 4. Run the Container

```bash
docker run -p 8000:8000 nemo-asr-app
```

---

## API Usage

### Endpoint

`POST /transcribe`

- **Request:** Multipart form with a `.wav` file (16kHz, 5 seconds).
- **Response:** JSON with the transcribed text.

### Example Request

```bash
python app/test.py
```

**Sample Response:**
```json
{
  "transcription": "▁मशीन▁लर्नििंग▁की▁फील्ड▁में▁▁डेटा▁प्रोसेसिंग▁बहुतत▁इंपॉर्टेंट▁है▁जैसे▁कि▁डेटा▁क्लीनिंग▁▁फीचर्▁स्कीलिंग▁और▁मिसिंग▁काली▁उस▁कोो▁हैंडलल▁करना▁इन▁टास्क▁को▁को▁एफिशििएंटी▁परफॉर्म▁करने▁के▁लिएए▁व्हहाइट▁हैट▁में▁लाइब्र्रेरी▁जैसे▁प्ैंडर्स▁और▁नंबर▁ययूज▁किए▁जाते▁हैं▁अगर▁आपको▁मॉडर्ल▁▁ट्र्रेनिंग▁करनीी▁है▁तो▁साइकिल▁एक▁पॉपुलर▁चॉइसस▁है"}

```

---

## Design Considerations

- **ONNX Runtime** for efficient inference.
- **FastAPI** for modern, async-ready web serving.
- **Strict Input Validation** for audio format and duration.
- **Containerization** for reproducible deployment.

---

## CI/CD & Azure Deployment

This project uses GitHub Actions for continuous integration and deployment. On every push to the `main` branch, the application is automatically built, tested, and deployed live to Azure Web Apps using a containerized workflow.

- **CI:** Automated Container Building via GitHub Actions.
- **CD:** Docker image is built and pushed to DockerHub, then deployed to Azure App Service.


## Limitations

- Only `.wav` files at 16kHz, of atleast 5 seconds duration are accepted.
- No GPU support in the provided Dockerfile.
- Hindi transcription only.