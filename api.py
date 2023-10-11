import openai
import os


def get_result(filepath, model_type, transform_mode):
    if model_type == "Local":
        # Make unimplemented error
        return

    openai.api_base = os.getenv("OPENAI_API_BASE") + "/v1"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    audio_file = open(filepath, "rb")

    if transform_mode == "Transcriptions":
        result = openai.Audio.transcribe("whisper-1", audio_file)
        return [result, result["text"]]

    result = openai.Audio.translate("whisper-1", audio_file)
    return [result, result["text"]]
