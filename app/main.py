from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.inference import transcribe_audio
from app.utils import validate_audio
import tempfile

app = FastAPI()


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Only .wav files are supported")

    print(f"Received file: {file.filename}, size: {file.size} bytes")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        content = await file.read()
        temp.write(content)
        temp.flush()

        duration_ok = validate_audio(temp.name)
        if not duration_ok:
            raise HTTPException(status_code=400, detail="Audio must be 5 seconds long")

        text = transcribe_audio(temp.name)
        return JSONResponse(content={"transcription": text})
