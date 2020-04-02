import os
import shutil
import logging

logger = logging.getLogger("file_copy")
logger.setLevel(logging.INFO)
fh = logging.FileHandler('file_copy.log', encoding='utf-8')
logger.addHandler(fh)

file_source = '/files_source'
file_copies = '/file_copies'

interseption = 2  # количество совпадающих частей имени

dir_ = os.getcwd()
files_origins = os.listdir(dir_ + f'{file_source}')
files = {file.lower().split('.')[0]: file for file in files_origins}

with open('names.bat', 'r', encoding='utf-8') as names:
    all_names = [set(name.split()) for name in map(lambda x: x.strip().lower(), names.readlines())]

for name in all_names:
    logger.info(f"Cheking name: {name}")
    amount = 0
    for file in files:
        file_set = set(file.split())
        current = name.intersection(file_set)
        if len(current) >= interseption:
            shutil.copyfile(dir_ + f'{file_source}/{files[file]}', dir_ + f'{file_copies}/{files[file]}')
            logger.info(f"Copy file \"{files[file]}\" - SUCCESS")
            amount += 1

    logger.info(f"Number of copied files for {name} - {amount}\n")

