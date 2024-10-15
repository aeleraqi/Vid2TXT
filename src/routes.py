import requests
from fastapi import APIRouter, HTTPException
from src.audio_processing import process_audio_file
import os

router = APIRouter()
@router.post("/process-audio/")
async def process_audio(file_url: str, language: str = "en"):
    """
    Endpoint to process the audio file from a URL.
    Supports multiple languages for speech recognition.
    """
    # Download the audio file from the given URL
    audio_file_path = "temp_audio.m4a"
    try:
        response = requests.get(file_url)
        response.raise_for_status()  # Check if the download was successful
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to download audio file: {e}")

    # Process the audio file to get recognized text and timestamps
    output_data = process_audio_file(audio_file_path, language)

    # Clean up the temporary audio file
    os.remove(audio_file_path)

    return {"message": "Processing completed", "output": output_data}