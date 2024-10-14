from pydub import AudioSegment
from pydub.silence import split_on_silence
from speech_recognition_utils import recognize_speech_google
from datetime import datetime, timedelta

def process_audio_file(audio_file: str):
    """
    Process an audio file to recognize speech and return the output data.
    """
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Split audio into chunks based on silence
    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

    output_data = []
    start_time = datetime.now()

    # Process each chunk
    for chunk in chunks:
        # Export each chunk to a temporary wav file
        chunk.export("temp.wav", format="wav")

        # Recognize speech from the exported chunk
        text = recognize_speech_google("temp.wav")

        # Calculate timestamp for the chunk
        duration = timedelta(seconds=chunk.duration_seconds)
        end_time = start_time + duration
        timestamp = end_time.strftime("%H:%M:%S")

        # Append timestamp and recognized text to the output data
        output_data.append((timestamp, text))

        # Update start time for the next chunk
        start_time = end_time

    return output_data
