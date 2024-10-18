import requests
from flask import Blueprint, request, jsonify
from src.audio_processing import process_audio_file
import os

router = Blueprint('api', __name__)

@router.route("/process-audio/", methods=["POST"])
def process_audio():
    """
    Endpoint to process the audio file from a URL.
    Supports multiple languages for speech recognition.
    """
    data = request.get_json()  # Get JSON data from the request
    file_url = data.get("file_url")
    language = data.get("language", "en")

    # Download the audio file from the given URL
    audio_file_path = "temp_audio.m4a"
    try:
        response = requests.get(file_url)
        response.raise_for_status()  # Check if the download was successful
        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.content)
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to download audio file: {e}"}), 400

    # Process the audio file to get recognized text and timestamps
    output_data = process_audio_file(audio_file_path, language)

    # Clean up the temporary audio file
    os.remove(audio_file_path)

    return jsonify({"message": "Processing completed", "output": output_data})