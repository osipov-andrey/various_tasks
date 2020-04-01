import os
import shutil

file_source = '/files_source'
file_copies = '/file_copies'

dir_ = os.getcwd()
files_origins = os.listdir(dir_ + f'{file_source}')
files = {file.lower(): file for file in files_origins}
print(files)

with open('names.bat', 'r', encoding='utf-8') as names:
    all_names = [name for name in map(lambda x: x.strip().lower(), names.readlines())]
    print(all_names)

for name in all_names:

    for file in files:

        if (name in file) and (name + 'а' not in file):
            shutil.copyfile(dir_ + f'{file_source}/{files[file]}', dir_ + f'{file_copies}/{files[file]}')

