import customtkinter as ctk
from lib.selectFile import select_file
from lib.audio_processing import process_audio_file
import os
import threading
from datetime import datetime, timedelta
from pydub.silence import split_on_silence
from pydub import AudioSegment
from CTkTable import *

data = {
    "file_url": '',
}

def check():
    if data["file_url"] != '':
        process_button.configure(state='normal')
    else:
        process_button.configure(state='disabled')

def process():
    def run_processing():
        process_button.configure(state='disabled', text="الصبر...هانت")
        # Perform the audio processing
        # Split audio into chunks based on silence
        audio = AudioSegment.from_file(data["file_url"])
        chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)
        output_data = []
        start_time = datetime.now()
        # Process each chunk
        for chunk in chunks:
            # Export each chunk to a temporary wav file
            chunk.export("temp.wav", format="wav")
            # Recognize speech from the exported chunk
            text = process_audio_file("temp.wav", 'ar-EG')
            # Calculate timestamp for the chunk
            duration = timedelta(seconds=chunk.duration_seconds)
            end_time = start_time + duration
            timestamp = end_time.strftime("%H:%M:%S")
            # Append timestamp and recognized text to the output data
            output_data.append((timestamp, text))
            # Update start time for the next chunk
            start_time = end_time
        # Clear previous content and display the new output data
        for widget in output_frame.winfo_children():
            widget.destroy()
        table = CTkTable(master=output_frame, row=len(output_data), column=2, values=output_data)
        os.remove('temp.wav')
        table.pack(expand=True, fill="both", padx=20, pady=20)
        process_button.configure(text="دوس", state='enabled')

    # Run the processing in a separate thread to avoid blocking the UI
    processing_thread = threading.Thread(target=run_processing)
    processing_thread.start()

def open_file():
    # Attempt to select a file
    file_path = select_file()
    # Update the data dictionary with the selected file path
    data.update({'file_url': file_path})
    # Update the button text to show the selected file path
    file_name = os.path.basename(file_path)
    open_button.configure(text=file_name)
    check()

# Set the appearance and theme
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark

# Create the main application window
app = ctk.CTk()
app.geometry("600x400")
app.title("يلا نحول ملف الصوت لكلام مكتوب")

# Create a frame to hold the widgets
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add a title label to the frame
title_label = ctk.CTkLabel(frame, text="يلا نحول ملف الصوت لكلام مكتوب", font=("tahoma", 20))
title_label.pack(pady=10)

# Create the open file button
open_button = ctk.CTkButton(
    frame,
    text='الملف',
    command=open_file,
    font=("tahoma", 20)
)
open_button.pack(expand=True)

# Create the process button
process_button = ctk.CTkButton(
    frame,
    text='دوس',
    command=process,
    state="disabled",
    font=("tahoma", 20)
)
process_button.pack(expand=True)

# Create a scrollable frame for the output
output_frame = ctk.CTkScrollableFrame(frame)
output_frame.pack(pady=20, fill="both", expand=True)

# Run the application
app.mainloop()