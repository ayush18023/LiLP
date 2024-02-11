import PyPDF2

def mergeFiles(pdfFiles):
    import time
    pdfWriter = PyPDF2.PdfWriter()
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        for pageNum in range(0, len(pdfReader.pages)):
            pageObj = pdfReader.pages[pageNum]
            pdfWriter.add_page(pageObj)
    
    splitted = pdfFiles[0].split("/")
    pathName = '/'.join(splitted[:len(splitted)-1])

    outputName = pathName + "/merge" + str(int(time.time())) + ".pdf"
    # print(outputName)
    pdfOutput = open(outputName, 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
