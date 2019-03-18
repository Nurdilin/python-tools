import PyPDF2
import os

from PyPDF2 import PdfFileReader, PdfFileMerger

pdfs = ['test1.pdf', 'test2.pdf', 'test3.pdf' ]


merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("all.pdf")

    


#files = [x for x in os.listdir('.') if x.endswith('.pdf')]

#for fname in sorted(files):
#    merger.append(PdfFileReader(open(
#        os.path.join('.', fname), 'rb')))

