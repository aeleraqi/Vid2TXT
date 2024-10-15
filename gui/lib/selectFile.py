from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
def select_file():
    filetypes = (
        ('Audio Files', '*.m4a'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )