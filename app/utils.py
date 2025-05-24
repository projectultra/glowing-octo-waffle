import librosa
import numpy as np
import asyncio
import aiofiles
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor()


async def validate_audio(path):
    y, sr = await asyncio.get_event_loop().run_in_executor(
        _executor, lambda p: librosa.load(p, sr=16000), path
    )
    duration = librosa.get_duration(y=y, sr=sr)
    return 5.0 <= duration


async def preprocess_audio(path):
    sample_rate = 16000
    samples, _ = await asyncio.get_event_loop().run_in_executor(
        _executor, lambda p: librosa.load(p, sr=sample_rate), path
    )
    samples = samples * 32768  # scaling
    mel_spec = librosa.feature.melspectrogram(
        y=samples, sr=sample_rate, n_mels=80, n_fft=512, hop_length=160, win_length=400
    )
    log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
    mean = log_mel_spec.mean(axis=0, keepdims=True)
    stddev = log_mel_spec.std(axis=0, keepdims=True)
    features = (log_mel_spec - mean) / (stddev + 1e-5)
    return np.expand_dims(features, axis=0)


async def load_token_map(token_file="model/tokens.txt"):
    token_map = {}
    async with aiofiles.open(token_file, encoding="utf-8") as f:
        async for line in f:
            if line.strip():
                token, idx = line.strip().split()
                token_map[int(idx)] = token
    return token_map


def decode_tokens(token_ids, token_map):
    # Remove <blk> (usually blank token in CTC, here index 128)
    return "".join([token_map[tok] for tok in token_ids if tok != 128])
