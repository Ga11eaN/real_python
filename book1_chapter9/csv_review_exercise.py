import csv
import os


my_file = r'D:\python\real_python_materials\book1-exercises\chp09\practice_files\pastimes.csv'
my_output_file = r'D:\python\real_python_materials\book1-exercises\chp09\practice_files\categorized pastimes.csv'

with open(my_file, 'r') as fh, open(my_output_file, 'w') as output_fh:
    file_text = csv.reader(fh)
    header = next(file_text)
    header.append('Type of Pastime')
    file_writer = csv.writer(output_fh)
    file_writer.writerow(header)
    for line in file_text:
        if line[1].lower().find('fighting') != -1:
            line.append('Combat')
        else:
            line.append('Other')
        file_writer.writerow(line)
