import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

def process_audio_file(audio_file_path):
    """
    Process the audio file to recognize speech and return recognized text with timestamps.
    """
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Split audio into chunks based on silence
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

    output_data = []
    recognizer = sr.Recognizer()

    # Process each chunk
    for i, chunk in enumerate(chunks):
        # Export each chunk to a temporary wav file
        chunk.export("temp_chunk.wav", format="wav")

        # Recognize speech from the exported chunk
        with sr.AudioFile("temp_chunk.wav") as source:
            audio_data = recognizer.record(source)
            try:
                # Recognize the audio, assuming the language is Arabic
                text = recognizer.recognize_google(audio_data, language='ar-EG')
            except sr.UnknownValueError:
                text = "(Could not understand)"
            except sr.RequestError as e:
                text = f"(Error: {e})"

        # Calculate the timestamp for the chunk
        timestamp = i * chunk.duration_seconds

        # Append recognized text and timestamp to output data
        output_data.append({"timestamp": timestamp, "text": text})

    # Clean up temporary file
    os.remove("temp_chunk.wav")

    return output_data