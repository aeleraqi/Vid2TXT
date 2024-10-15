import customtkinter as ctk
from lib.selectFile import select_file

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
open_button = ctk.CTkButton(
    frame,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

# Run the application
app.mainloop()