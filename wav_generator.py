import pyaudio
import wave

# Parameters for recording
FORMAT = pyaudio.paInt16  # Format for recording (16-bit resolution)
CHANNELS = 1              # Number of channels (1 for mono, 2 for stereo)
RATE = 44100              # Sampling rate (44.1 kHz for CD quality)
CHUNK = 1024              # Size of each chunk of audio data
RECORD_SECONDS = 30       # Duration to record (in seconds)
OUTPUT_FILENAME = "output.wav"  # Output file name

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream for recording
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Record audio in chunks and store it
frames = []
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio session
audio.terminate()

# Save the recorded audio as a .wav file
with wave.open(OUTPUT_FILENAME, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))

print(f"Audio recorded and saved as {OUTPUT_FILENAME}")
