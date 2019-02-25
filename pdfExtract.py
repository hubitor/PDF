import PyPDF2
pdfFileObj = open('Lineup.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
#print(pdfReader.numPages)
pageObj = pdfReader.getPage(2)
pageObj.extractText()
print(pageObj.extractText())
