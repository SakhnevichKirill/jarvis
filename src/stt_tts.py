
import config

class STTPipeline:
    def __init__(self):
        self.pipeline = config.stt_pipeline
    
    def transcribe(self, audio_path):
        transcript = self.pipeline(
            audio_path=audio_path,
            chunk_length_s=30,
            stride_length_s=5,
            max_new_tokens=128,
            batch_size=100,
            language="english",
            return_timestamps=False,
        )
        return transcript['text']


class TTSPipeline:
    def __init__(self):
        self.tts = config.tts
    
    def synthesize(self, text, output_path):
        self.tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=config.TTS_SETTINGS['speaker_wav'],
            language=config.TTS_SETTINGS['language']
        )