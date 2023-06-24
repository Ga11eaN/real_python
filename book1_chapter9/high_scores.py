import csv


my_path = r"D:\python\real_python_materials\book1-exercises\chp09\practice_files\scores.csv"

with open(my_path, 'r') as fh:
    file_text = csv.reader(fh)

    high_score_dict = {}
    for row in file_text:
        key = row[0]
        value = row[1]
        if row[0] not in high_score_dict:
            high_score_dict[key] = value
        elif int(high_score_dict[key]) < int(value):
            high_score_dict[key] = value

    print(sorted(high_score_dict.items()))
