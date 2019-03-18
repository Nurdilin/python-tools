import PyPDF2
from PyPDF2 import PdfFileReader

pdf = open ("example.pdf", 'rb')
reader = PdfFileReader(pdf)


print "PDF Reader object is:", reader
print "Number of pages:", reader.getNumPages()
print "Title:          ", reader.getDocumentInfo().title
print "Author:         ", reader.getDocumentInfo().author

print "Book Outline"
for heading in reader.getOutlines():
    if type(heading) is not list:
        print dict(heading).get('/Title')

