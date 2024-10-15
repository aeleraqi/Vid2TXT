from tkinter import filedialog as fd

def select_file():
    filetypes = (
        ('Audio Files', '*.m4a'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    if filename:  # If a file is selected, return its path
        return filename
    else:  # Raise an error if no file is selected
        raise FileNotFoundError("No file was selected.")