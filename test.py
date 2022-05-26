#! /usr/bin/python3.6
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime, timedelta

laiks = datetime.strftime(datetime.now() + timedelta(1), '%Y%m%d') # PDF faila laika nosaukuma formāts 20220505 šodien + 1 diena.
laiksMape = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d') # Mapes laika nosaukuma formāts 2022-05-05 šodien + 1 diena.

# Split PDF - PDF failu sagriež.
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    rangeEnd = pdf.getNumPages()
    rangeStart = 0
    for pageNumber in range(rangeStart, rangeEnd ):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(pageNumber))

        fileprefix = "0" + str(pageNumber+1)
        if pageNumber >8:
            fileprefix = str(pageNumber+1)

        output_filename = "/var/files/DIENA/" + str(laiksMape) + "/{}_{}_{}.pdf".format(
            fname, laiks, fileprefix) # Pieliekās faila nosaukums + laika formāts + lapas nr. pēc kārtas.
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

path ="/var/files/DIENA/" + str(laiksMape) + "/DIENA.pdf"
pdf_splitter(path)

os.remove("/var/files/DIENA/"+ (laiksMape) +"/DIENA.pdf")

os.system('php /var/www/html/nextcloud/occ files:scan --all')
