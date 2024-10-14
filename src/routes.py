from fastapi import APIRouter, UploadFile, File
from audio_processing import process_audio_file
import os

router = APIRouter()

@router.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    """
    Endpoint to process the uploaded audio file.
    """
    # Save the uploaded file
    audio_file_path = f"temp_{file.filename}"
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(await file.read())

    # Process the audio file to get recognized text and timestamps
    output_data = process_audio_file(audio_file_path)


    # Clean up the temporary audio file
    os.remove(audio_file_path)

    return {"message": "Processing completed", "output": output_data}
