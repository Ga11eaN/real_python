import os
from PyPDF2 import PdfReader, PdfWriter


path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"

input_file_name = os.path.join(path, 'Pride and Prejudice.pdf')
input_file = PdfReader(open(input_file_name, 'rb'))

output_pdf = PdfWriter()

for page_num in range(1, 4):
    output_pdf.add_page(input_file.pages[page_num])

with open('lecture_output.pdf', 'wb') as output_file:
    output_pdf.write(output_file)

from PyPDF2 import PdfReader, PdfWriter
import copy
import os

path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"
input_file = PdfReader(open(path + '\\half and half.pdf', 'rb'))
output_pdf = PdfWriter()

for page_num in range(len(input_file.pages)):
    page_left = input_file.pages[page_num]
    page_right = copy.copy(page_left)
    upper_right = page_left.mediabox.upper_right

    page_left.mediabox.upper_right = (upper_right[0] / 2, upper_right[1])
    output_pdf.add_page(page_left)

    page_right.mediabox.upper_left = (upper_right[0] / 2, upper_right[1])
    output_pdf.add_page(page_right)

output_file_name = 'The little Mermaid.pdf'
output_file = open(output_file_name, 'wb')
output_pdf.write(output_file)
output_file.close()

import os
from PyPDF2 import PdfReader, PdfWriter


path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"
input_file_name = os.path.join(path, "The Emperor.pdf")
input_file = PdfReader(open(input_file_name, "rb"))
output_PDF = PdfWriter()

watermark_file_name = os.path.join(path, "top secret.pdf")
watermark_file = PdfReader(open(watermark_file_name, "rb"))

for page_num in range(0, len(input_file.pages)):
    page = input_file.pages[page_num]
    page.merge_page(watermark_file.pages[0]) # add watermark image
    output_PDF.add_page(page)

output_PDF.encrypt("good2Bking") # add a password to the PDF file
output_file_name = "New Suit.pdf"
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()