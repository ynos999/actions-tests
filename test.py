#! /usr/bin/python3.6
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime, timedelta

laiks = datetime.strftime(datetime.now() + timedelta(1), '%Y%m%d') 
laiksMape = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')

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

        output_filename = "/var/www/html/" + str(laiksMape) + "/{}_{}_{}.pdf".format(
            fname, laiks, fileprefix)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

path ="/var/www/html/" + str(laiksMape) + "/DIENA.pdf"
pdf_splitter(path)

os.remove("/var/www/html/"+ (laiksMape) +"/DIENA.pdf")

os.system('php /var/www/html/nextcloud/occ files:scan --all')
