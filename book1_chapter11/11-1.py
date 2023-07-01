import os
from PyPDF2 import PdfWriter, PdfReader

path = r"D:\python\real_python_materials\book1-exercises\chp11\practice_files"

input_file_name = os.path.join(path, 'The Whistling Gypsy.pdf')
with open(input_file_name, 'rb') as input_file:
    reader = PdfReader(input_file)
    total_pages = len(reader.pages)
    print('Title: ', reader.metadata.title)
    print('Author: ', reader.metadata.author)
    print('NUmber of pages: ', total_pages)

    with open("output_txt.txt", 'wb') as output_txt:
        for page_num in range(total_pages):
            text = reader.pages[page_num].extract_text()
            text = text.replace("  ", "\n").encode('utf-8')
            output_txt.write(text)

    with open("output_pdf.pdf", 'wb') as output_pdf:
        for page_num in range(1, total_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
        writer.write(output_pdf)
