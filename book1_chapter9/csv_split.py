import argparse
import csv
import os
import sys


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise Exception(f'File {file_path} does not exists!')


def check_file_rows(file_path, rows_limit):
    num_lines = sum(1 for _ in open(file_path))
    if num_lines - 1 < rows_limit:
        raise Exception('Row limit is > than rows quantity in the file!')
    return num_lines - 1


def get_arguments():
    parser = argparse.ArgumentParser(description='Parsing csv file by chunks')
    parser.add_argument('-i', '--input', help='input file name', type=str)
    parser.add_argument('-o', '--output', help='output file name', type=str)
    parser.add_argument('-r', '--row_limit', help='row limit to split', type=int)

    return vars(parser.parse_args())


MY_PATH = r"D:\python\real_python_materials\book1-exercises\chp09\solutions\sample_csv.csv"

arguments = get_arguments()
input_file_path = arguments['input']
output_file_path = arguments['output']
row_limit = arguments['row_limit']

check_file_exists(input_file_path)
rows_input_file = check_file_rows(input_file_path, row_limit)

with open(input_file_path, 'r') as fh:
    reader = csv.reader(fh)
    header = next(reader)
    chunks = rows_input_file // row_limit

    rows_in_chunk = row_limit
    chunk = 0
    writer_handler = 0

    for row in reader:
        if rows_in_chunk == row_limit:
            rows_in_chunk = 0
            chunk += 1
            output_file_name = output_file_path.split('.')[0] + f'_chunk_{chunk}.' + output_file_path.split('.')[1]
            if writer_handler:
                writer_handler.close()
            writer_handler = open(output_file_name, 'w', newline='')
            file_writer = csv.writer(writer_handler)
            file_writer.writerow(header)
        rows_in_chunk += 1
        file_writer.writerow(row)
    writer_handler.close()
