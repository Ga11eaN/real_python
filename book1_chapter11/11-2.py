from PyPDF2 import PdfReader, PdfWriter
import os
import copy


path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"
input_file_path = '\\Walrus.pdf'
input_file = os.path.join(path + input_file_path)
input_file_pdf = PdfReader(open(input_file, 'rb'))
input_file_pdf.decrypt('IamtheWalrus')

output_file_name = 'Walrus.pdf'
output_file_pdf = PdfWriter()

for page_num in range(len(input_file_pdf.pages)):
    page = input_file_pdf.pages[page_num].rotate(270)
    page_right = copy.copy(page)
    upper_right = page.mediabox.upper_right
    
    page.mediabox.upper_right = (upper_right[0]/2, upper_right[1])
    output_file_pdf.add_page(page)

    page_right.mediabox.upper_left = (upper_right[0]/2, upper_right[1])
    output_file_pdf.add_page(page_right)

with open(output_file_name, 'wb') as output_file:
    output_file_pdf.write(output_file)


