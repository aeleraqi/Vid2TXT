import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
def process_audio_file(file_path: str, language: str = "en"):
    """
    Process the audio file to perform speech recognition.
    Supports multiple languages.
    """
    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Convert the audio to WAV format for processing
    wav_file_path = "temp_audio.wav"
    audio.export(wav_file_path, format="wav")

    # Perform speech recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            # Recognize speech using the specified language
            text = recognizer.recognize_google(audio_data, language=language)
        except sr.UnknownValueError:
            text = "Speech recognition could not understand the audio."
        except sr.RequestError as e:
            text = f"Could not request results from the speech recognition service; {e}"

    # Clean up the temporary WAV file
    os.remove(wav_file_path)

    return text