# Project Description

## Features Successfully Implemented

- **ONNX Model Integration:** Integrated the `stt_hi_conformer_ctc_medium.onnx` model for Hindi speech-to-text inference.
- **FastAPI Service:** Developed a FastAPI application with a `/transcribe` endpoint for audio transcription.
- **Input Validation:** Implemented checks for `.wav` file type, 16kHz sampling rate, and minimum duration.
- **Async Inference Pipeline:** The API is async-ready for efficient request handling.
- **Containerization:** Provided a Dockerfile for easy deployment.
- **Documentation:** Included clear setup, usage, and design documentation.

## Issues Encountered

- **Lack of Model Documentation:** The NVIDIA NeMo model had almost no documentation especially for ONNX, making integration and usage challenging.
- **Dependency Resolution:** Required dependencies for model export and inference were not clearly listed; I had to manually identify and install them one by one.
- **Audio Format Ambiguity:** The model documentation only mentioned the sampling rate, with no details about required audio normalization or other preprocessing steps.
- **ONNX Export Compatibility:** Some preprocessing steps required adjustment to match the ONNX model's input expectations.
- **Audio Validation:** Ensuring robust validation for audio duration and format required extra handling.
- **No GPU Support in Docker:** The current Dockerfile does not support GPU acceleration due to base image and deployment constraints.

## Unimplemented Components & Limitations

- **GPU Inference:** GPU support was not implemented due to the complexity of CUDA setup in Docker and limited testing resources.
- **Model Optimization:** The ONNX model is not optimized for size or speed; future work could include quantization or pruning.

## Plans to Overcome Challenges

- **GPU Support:** Future versions can use NVIDIA’s CUDA-enabled Docker base images and ONNX Runtime GPU for faster inference.

## Known Limitations & Assumptions

- Only `.wav` files at 16kHz and at least 5 seconds long are accepted.
- The service only supports Hindi transcription.
- The container runs on CPU only.
- Users must manually download and place the ONNX model and tokens file in the `model/` directory.

---

For setup and usage, see [README.md](README.md).