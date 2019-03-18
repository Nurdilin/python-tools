import sys
import PyPDF2
from PyPDF2 import PdfFileReader

page = int(sys.argv[1])

pdf = open ("example.pdf", 'rb')
reader = PdfFileReader(pdf)

page = reader.getPage(page)
print page.extractText()
