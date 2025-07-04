from RealtimeTTS import TextToAudioStream, PiperEngine, PiperVoice
import time

def dummy_generator():
    # yield "This is piper tts speaking."
    yield "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. These machines can learn from experience, adjust to new inputs, and perform human-like tasks. AI encompasses a wide range of technologies, including machine learning, deep learning, and natural language processing. "

voice = PiperVoice(
    model_file=r"piper\voices_external\en_GB-southern_english_female-low.onnx",
    config_file=r"piper\voices_external\en_en_GB_southern_english_female_low_en_GB-southern_english_female-low.onnx.json",
)

engine = PiperEngine(
    piper_path="piper\piper.exe",
    voice=voice,
)

start = time.time()
stream = TextToAudioStream(engine)
stream.feed(dummy_generator())
end = time.time()
print(f"Time taken to generate audio: {end - start} seconds")
stream.play(output_wavfile="output.wav")
