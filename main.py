import os
import pvporcupine
import pvrecorder
import struct
import speech_recognition as sr
from dotenv import load_dotenv
from brain.agent_core import AstroAgent

load_dotenv()
agent = AstroAgent()

# Wake word "hmm" detector
porcupine = pvporcupine.create(
    keywords=["hmm"],
    access_key=os.getenv("PORCUPINE_API_KEY")
)

recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🤖 hmm agent awake. Say 'hmm' to activate...")

try:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    
    while True:
        # Listen for "hmm"
        pa = pvrecorder.PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
        pa.start()
        
        while True:
            pcm = pa.read()
            keyword_index = porcupine.process(struct.unpack_from("h" * porcupine.frame_length, pcm))
            if keyword_index >= 0:
                print("🔥 WAKE WORD 'hmm' DETECTED!")
                pa.stop()
                break
        
        # Speech-to-text after wake word
        with mic as source:
            audio = recognizer.listen(source, timeout=5)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"🗣️  You said: {command}")
            response = agent.process(command)
            print(f"🧠 AstroBrain: {response}")
        except sr.UnknownValueError:
            print("❓ Didn't catch that...")
        
finally:
    pa.stop()
    porcupine.delete()
