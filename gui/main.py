import customtkinter as ctk
from lib.selectFile import select_file
import os

data = {
    "file_url": '',
    "language": ""
}

def open_file():
    try:
        # Attempt to select a file
        file_path = select_file()
        # Update the data dictionary with the selected file path
        data.update({'file_url': file_path})
        # Update the button text to show the selected file path
        file_name = os.path.basename(file_path)
        open_button.configure(text=file_name)
    except FileNotFoundError:
        # Display the error message if no file was selected
        print("No file")

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

open_button.pack(expand=True)

# Run the application
app.mainloop()