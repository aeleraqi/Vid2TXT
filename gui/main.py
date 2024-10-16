import customtkinter as ctk
from lib.selectFile import select_file
from lib.audio_processing import process_audio_file
import os
import threading
from textwrap import wrap
from awesometkinter.bidirender import render_bidi_text, add_bidi_support

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
        process_button.configure(state='disabled', text="WAIT A FEW SECONDS...")
        # Perform the audio processing
        output = process_audio_file(data["file_url"], 'ar-EG')
        print(output)
        
        # Update the UI after processing
        output_textbox.configure(state="normal")  # Enable editing to insert text
        output_textbox.delete("1.0", ctk.END)  # Clear previous output
        
        # Reverse the text content for RTL languages
        output = '\n'.join(wrap(output, 50))
        output = render_bidi_text(output)  # Correctly render bidi text
        output_textbox.insert("1.0", output)
        output_textbox.tag_add("center", "1.0", "end")
        
        output_textbox.configure(state="disabled")  # Disable editing again
        process_button.configure(text="CONVERT", state='enabled')

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
app.title("CONVERT YOUR AUDIO TO TEXT")

# Create a frame to hold the widgets
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add a title label to the frame
title_label = ctk.CTkLabel(frame, text="CONVERT YOUR AUDIO TO TEXT", font=("Arial", 20))
title_label.pack(pady=10)

# Create the open file button
open_button = ctk.CTkButton(
    frame,
    text='Open a File',
    command=open_file
)
open_button.pack(expand=True)

# Create the process button
process_button = ctk.CTkButton(
    frame,
    text='CONVERT',
    command=process,
    state="disabled"
)
process_button.pack(expand=True)

# Create a frame for the output text area
output_frame = ctk.CTkFrame(frame)
output_frame.pack(pady=20, fill="both", expand=True)

# Create a scrollable text area for output
output_textbox = ctk.CTkTextbox(output_frame, wrap="word", font=('tahoma', 15))
output_textbox.configure(state="disabled")
output_textbox.pack(side="left", fill="both", expand=True)

# Add bidirectional support to the output_textbox
add_bidi_support(output_textbox)

# Create a vertical scrollbar for the text area
scrollbar = ctk.CTkScrollbar(output_frame, command=output_textbox.yview)
scrollbar.pack(side="right", fill="y")

# Configure the textbox to work with the scrollbar
output_textbox.configure(yscrollcommand=scrollbar.set)

# Run the application
app.mainloop()