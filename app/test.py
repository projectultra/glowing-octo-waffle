import httpx
import asyncio


async def send_audio():
    url = "http://localhost:8000/transcribe"
    file_path = "audio/sample.wav"

    async with httpx.AsyncClient() as client:
        with open(file_path, "rb") as f:
            files = {"file": ("sample.wav", f, "audio/wav")}
            response = await client.post(url, files=files, timeout=60)

        print("Status code:", response.status_code)
        print("Response:", response.text)


asyncio.run(send_audio())
