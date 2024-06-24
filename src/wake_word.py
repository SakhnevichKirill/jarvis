import sounddevice as sd
import numpy as np
import pvporcupine

def wake_word_detect(wake_word="jarvis", access_key="YOUR_ACCESS_KEY_HERE"):
    porcupine = pvporcupine.create(keywords=[wake_word], access_key=access_key)
    with sd.InputStream(samplerate=16000, channels=1, dtype='int16') as stream:
        print("Listening for wake word...")
        while True:
            audio_frame, _ = stream.read(porcupine.frame_length)
            audio_frame = audio_frame.flatten()
            audio_frame = np.array(audio_frame, dtype=np.int16)
            keyword_index = porcupine.process(audio_frame)
            if keyword_index >= 0:
                print("Wake word detected!")
                return
