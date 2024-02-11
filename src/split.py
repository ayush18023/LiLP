import PyPDF2

def splitFile(file, start, end):
    import time
    pdfWriter = PyPDF2.PdfWriter()
    pdfFileObj = open(file, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    for pageNum in range(start-1, end):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

    splitted = file.split("/")
    pathName = '/'.join(splitted[:len(splitted)-1])

    outputName = pathName + "/split" + str(int(time.time())) + ".pdf"
    pdfOutput = open(outputName, 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()