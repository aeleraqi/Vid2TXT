import customtkinter as ctk
from lib.selectFile import select_file
from lib.audio_processing import process_audio_file
from lib.lang import speech_recognition_languages as languages
import os

data = {
    "file_url": '',
    "language": "en-US"
}
def check():
    if data["file_url"] != '' and data['language']:
        process_button.configure(state='enabled')
    else:
        process_button.configure(state='disabled')
def process():
    output = process_audio_file(data["file_url"], data["language"])
    print("output: "+ output)

def open_file():
    # Attempt to select a file
    file_path = select_file()
    # Update the data dictionary with the selected file path
    data.update({'file_url': file_path})
    # Update the button text to show the selected file path
    file_name = os.path.basename(file_path)
    open_button.configure(text=file_name)
    check()

def on_select(event):
    selected_language = language_var.get()
    selected_language_code = languages[selected_language]
    data.update({'language': selected_language_code})
    print(f"Selected Language: {selected_language_code}")
    check()

# Set the appearance and theme
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark

# Create the main application window
app = ctk.CTk()
app.geometry("600x400")
app.title("Audio to text")

# Create a frame to hold the widgets
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add a title label to the frame
title_label = ctk.CTkLabel(frame, text="Convert your audio files to text", font=("Arial", 20))
title_label.pack(pady=10)

# Create the open file button
open_button = ctk.CTkButton(
    frame,
    text='Open a File',
    command=open_file
)
language_var = ctk.StringVar(value=list(languages.keys())[0])
dropdown = ctk.CTkOptionMenu(frame, variable=language_var, values=list(languages.keys()), command=on_select)
dropdown.pack(pady=20)
process_button = ctk.CTkButton(
    frame,
    text='Convert',
    command=process,
    state="disabled"
)

open_button.pack(expand=True)
process_button.pack(expand=True)

# Run the application
app.mainloop()