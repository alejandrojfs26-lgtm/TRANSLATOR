# Traductor de Voz Multilingüe

Aplicación web de traducción de voz que transcribe audio en español y genera audio traducido a 4 idiomas simultáneamente usando Whisper, Google Translate y gTTS.

## Tecnologías

- **Whisper (OpenAI)** — Transcripción de voz a texto
- **Gradio** — Interfaz web interactiva
- **gTTS** — Text-to-speech en múltiples idiomas
- **translate** — Traducción de texto (Google Translate)

## Idiomas destino

- Inglés
- Francés
- Portugués
- Alemán

## Requisitos

- Python 3.10+
- FFmpeg (necesario para Whisper)

### Instalar FFmpeg

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
winget install ffmpeg
```

## Instalación

```bash
git clone https://github.com/alejandrojfs26-lgtm/TRANSLATOR.git
cd TRANSLATOR

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

Abre el navegador en `http://localhost:7860`, graba un mensaje en español y obtén audio traducido en los 4 idiomas.

## Notas

- El modelo Whisper "base" (~1.4 GB) se descarga la primera vez
- La traducción usa Google Translate (requiere internet)
- Los archivos de audio se guardan en `audio/`

## Licencia

MIT
