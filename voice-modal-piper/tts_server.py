from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from RealtimeTTS import TextToAudioStream, PiperEngine, PiperVoice
import os

app = FastAPI()

# Add CORS middleware for remote access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up Jinja2 templates (for HTML UI)
templates = Jinja2Templates(directory="templates")

# Piper voice setup
voice = PiperVoice(
    model_file=r"piper/voices_external/en_GB-southern_english_female-low.onnx",
    config_file=r"piper/voices_external/en_en_GB_southern_english_female_low_en_GB-southern_english_female-low.onnx.json",
)

engine = PiperEngine(
    piper_path="piper/piper.exe",
    voice=voice,
)

# Route for HTML UI
@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# TTS audio generation route
@app.post("/tts")
async def tts(text: str = Form(...)):
    filename = "output.wav"
    
    def text_gen():
        yield text

    stream = TextToAudioStream(engine)
    stream.feed(text_gen())
    stream.play(output_wavfile=filename, muted=True)  # Generate file without playing audio

    return FileResponse(
        path=filename, 
        media_type="audio/wav", 
        filename="output.wav"
    )
