import whisper

model = whisper.load_model("base")  # Use "tiny" for faster, less accurate processing
result = model.transcribe("output.wav")
print("Transcript:", result["text"])
