import os
import glob


my_path = r'D:\python\real_python_materials\book1-exercises\chp09\practice_files\images'


for cur_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        current_filename = os.path.join(cur_folder, file_name)
        if current_filename.lower().endswith('jpg'):
            print(f'file {current_filename} exists: ', os.path.exists(current_filename))
