import onnxruntime as ort
import numpy as np
from app.utils import preprocess_audio, load_token_map, decode_tokens
import asyncio

ort_session = ort.InferenceSession("model/stt_hi_conformer_ctc_medium.onnx")


async def transcribe_audio(audio_path):
    input_tensor = await preprocess_audio(audio_path)
    input_length = np.array([input_tensor.shape[2]], dtype=np.int64)

    ort_inputs = {
        ort_session.get_inputs()[0].name: input_tensor,
        ort_session.get_inputs()[1].name: input_length,
    }

    loop = asyncio.get_event_loop()
    ort_outs = await loop.run_in_executor(None, ort_session.run, None, ort_inputs)

    decoded = np.argmax(ort_outs[0], axis=-1).squeeze()
    token_map = await load_token_map("model/tokens.txt")
    return decode_tokens(decoded, token_map)
