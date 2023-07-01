from PyPDF2 import PdfWriter, PdfReader
import os


def create_file_path(file_name):
    path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"
    return os.path.join(path, file_name)


input_file_path = create_file_path('The Emperor.pdf')
input_file_pdf = PdfReader(open(input_file_path, 'rb'))

input_cover_path = create_file_path('Emperor cover sheet.pdf')
input_cover_pdf = PdfReader(open(input_cover_path, 'rb'))

output_file_path = 'The Covered Emperor.pdf'
output_file_pdf = PdfWriter()

output_file_pdf.add_page(input_cover_pdf.pages[0])
for page in input_file_pdf.pages:
    output_file_pdf.add_page(page)

with open(output_file_path, 'wb') as output_file:
    output_file_pdf.write(output_file)
