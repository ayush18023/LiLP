from tkinter import filedialog

def singleFile(root):
    file = filedialog.askopenfilename(parent=root, title='Choose a file')
    return file

def selectFiles(root):
    pdfFiles = filedialog.askopenfilenames(parent=root, title='Choose files')
    return pdfFiles