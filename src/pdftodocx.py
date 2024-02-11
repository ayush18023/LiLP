from pdf2docx import Converter

def pdftodocx(file):
    cv = Converter(file)
    splitted = file.split(".")
    outputName = splitted[0] + ".docx"
    cv.convert(outputName, start=0, end=None)
    cv.close()