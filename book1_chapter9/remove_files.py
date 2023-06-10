import os


my_path = r'D:\python\real_python_materials\book1-exercises\chp09\practice_files\little pics'

for current_folder, sub_folder, file_names in os.walk(my_path):
    for file_name in file_names:
        if file_name.lower().endswith('jpg'):
            file_path = os.path.join(current_folder, file_name)
            if os.path.getsize(file_path) < 2000:
                os.remove(file_path)
