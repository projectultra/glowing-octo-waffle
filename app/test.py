import requests

url = "http://localhost:8000/transcribe"
file_path = "audio/sample.wav"

with open(file_path, "rb") as f:
    files = {"file": ("sample.wav", f, "audio/wav")}
    response = requests.post(url, files=files, timeout=10)

print("Status code:", response.status_code)
print("Response:", response.text)
