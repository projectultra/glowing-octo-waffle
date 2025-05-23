# https://colab.research.google.com/drive/1aDXpiLa_5OzSNHcPtSFe0suCs3ZPHHSR?usp=sharing
# Used Google Colab to convert the model to ONNX format
from nemo.collections.asr.models import EncDecCTCModel


def export():
    model = EncDecCTCModel.from_pretrained(model_name="stt_hi_conformer_ctc_medium")
    model.eval()
    model.export(
        output_path="stt_hi_conformer_ctc_medium.onnx",
        check_trace=False,
        input_names=["audio_signal", "length"],
        output_names=["logits"],
    )
    with open("tokens.txt", "w") as f:
        for i, s in enumerate(model.decoder.vocabulary):
            f.write(f"{s} {i}\n")
        f.write(f"<blk> {i+1}\n")


export()
