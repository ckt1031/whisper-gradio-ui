import os
import gradio as gr
from dotenv import load_dotenv

from api import get_result

load_dotenv()


def clear_value():
    gr.update(value=None)


with gr.Blocks(title="Whisper UI") as page:
    gr.Markdown("""# Whisper UI""")

    with gr.Row() as row1:
        with gr.Column(scale=1) as col1:
            model_type = gr.Radio(
                choices=["API", "Local"],
                label="Choose model type",
                value="API",
                interactive=False,
            )

        with gr.Column(scale=1) as col2:
            transform_mode = gr.Radio(
                choices=["Transcriptions", "Translations"],
                label="Choose transform mode",
                value="Transcriptions",
                interactive=True,
            )

    # Content
    with gr.Row() as row2:
        with gr.Column(scale=2, min_width=500) as row2_col1:
            # Audio
            with gr.Tab("Audio", id=2):
                audio_file_input = gr.Audio(
                    label="Audio",
                    sources=["upload", "microphone"],
                    type="filepath",
                    format="mp3",
                )
                with gr.Row():
                    audio_submit_button = gr.Button(
                        "Submit", elem_id="audio_submit_button"
                    )

    with gr.Column(scale=3, min_width=500, elem_id="output") as c2_2:
        with gr.Tab("Output Text", elem_id="output_text"):
            text_output = gr.Textbox(show_label=False, interactive=False)
        with gr.Tab("Output JSON", elem_id="output3"):
            json_output = gr.JSON(label="JSON")

    audio_submit_button.click(
        fn=get_result,
        inputs=[audio_file_input, model_type, transform_mode],
        outputs=[json_output, text_output],
    )


def simple_auth(_username, password):
    return password == os.getenv("AUTH_PASSWORD")


if os.getenv("AUTH_PASSWORD") is not None:
    page.launch(
        server_name="0.0.0.0", show_api=False, auth=simple_auth
    )
else:
    page.launch(server_name="0.0.0.0", show_api=False)
