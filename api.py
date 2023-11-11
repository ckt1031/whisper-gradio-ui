import os

from openai import OpenAI


def get_result(filepath, model_type, transform_mode):
    """Returns the audio result of the OpenAI API call"""
    if model_type == "Local":
        # Make unimplemented error
        return

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE") + "/v1",
    )

    audio_file = open(filepath, "rb")

    if transform_mode == "Transcriptions":
        result = client.audio.transcriptions.create(file=audio_file, model="whisper-1")
        return [result, result["text"]]

    result = client.audio.translations.create(file=audio_file, model="whisper-1")
    return [result, result["text"]]
