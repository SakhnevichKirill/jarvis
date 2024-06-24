import time
from config import CLIENT_HOST, AUDIO_DIR
from ollama import Client
from src.audio_processing import record_audio_vad, play_audio
from src.wake_word import wake_word_detect
from src.stt_tts import STTPipeline, TTSPipeline
from src.dialogue_manager import DialogueManager
import os

# Ensure necessary directories exist
os.makedirs(AUDIO_DIR, exist_ok=True)

def main():
    client = Client(host=CLIENT_HOST)
    stt_pipeline = STTPipeline()
    tts_pipeline = TTSPipeline()
    dialogue_manager = DialogueManager(client)
    
    while True:
        wake_word_detect()
        audio_path = os.path.join(AUDIO_DIR, "recorded_audio.wav")
        record_audio_vad(audio_path)

        transcript = stt_pipeline.transcribe(audio_path)
        print(transcript)

        response = dialogue_manager.handle_dialogue(transcript)
        print(response)
        
        tts_audio_path = os.path.join(AUDIO_DIR, "output.wav")
        tts_pipeline.synthesize(response, tts_audio_path)
        
        play_audio(tts_audio_path)

if __name__ == "__main__":
    main()