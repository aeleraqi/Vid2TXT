import speech_recognition as sr

def recognize_speech_google(audio_file: str) -> str:
    """
    Recognize speech from an audio file using Google Speech Recognition.
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Recognize the audio, assuming the language is Arabic
        text = recognizer.recognize_google(audio, language='ar-EG')
    except sr.UnknownValueError:
        text = "(Could not understand)"
    except sr.RequestError as e:
        text = f"(Error: {e})"

    return text