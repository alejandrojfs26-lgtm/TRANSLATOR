import gradio as gr
import whisper
from translate import Translator
from dotenv import load_dotenv
from gtts import gTTS
import os

load_dotenv(".env")

# idiomas destino disponibles
IDIOMAS = {
    "Inglés": "en",
    "Francés": "fr",
    "Portugués": "pt",
    "Alemán": "de",
}


def traducir_audio(audio_file):

    # trasncripcion texto
    # usamos whisper de openai: https://openai.com/index/whisper/ - https://github.com/openai/whisper
    # alternativa con https://assemblyai.com/

    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(f"Error al transcribir el audio: {str(e)}")

    if not transcription.strip():
        raise gr.Error("No se detectó voz en el audio. Intenta de nuevo.")

    archivos = []
    os.makedirs("audio", exist_ok=True)

    for nombre_idioma, lang_code in IDIOMAS.items():

        # traduccion texto
        # usamos translate: https://pypi.org/project/translate/   - https://github.com/terryyin/translate-python

        try:
            translator = Translator(from_lang="es", to_lang=lang_code)
            texto_traducido = translator.translate(transcription)
        except Exception as e:
            raise gr.Error(f"Error al traducir a {nombre_idioma}: {str(e)}")

        # generar audio traducido
        # usamos gTTS (Google Text-to-Speech): https://github.com/pndurette/gTTS

        try:
            save_file_path = f"/home/alejandro-fuentes/Proyectos Py/TRANSLATOR/audio/{lang_code}.mp3"
            tts = gTTS(text=texto_traducido, lang=lang_code)
            tts.save(save_file_path)
            archivos.append(save_file_path)
        except Exception as e:
            raise gr.Error(f"Error al generar audio en {nombre_idioma}: {str(e)}")

    return archivos


web = gr.Interface(
    fn=traducir_audio,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Graba tu voz"
    ),
    outputs=[
        gr.Audio(label="Inglés"),
        gr.Audio(label="Francés"),
        gr.Audio(label="Portugués"),
        gr.Audio(label="Alemán"),
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()
