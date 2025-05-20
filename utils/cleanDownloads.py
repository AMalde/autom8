import os
from pathlib import Path
import shutil

from helperFunctions import get_all_file_types_in_folder


def organiseFiles(search_root, file_type): 

    folder = ""
    number_of_files = 0
    file_type = file_type.lower()
    all_files = Path(search_root)
    for path in all_files.rglob('*'):
        if path.is_dir() and path.name == 'pdf_folder':
            print(f'Found {file_type} folder at: {path}')
            folder = path
        else: 
            folder = all_files / 'temporary sorted folders' / (file_type + '_folder')
            folder.mkdir(parents=True, exist_ok=True)
    
    for file in all_files.rglob('*'): 
        
        if file.is_file() and file.suffix.lower() == '.'+file_type:
            number_of_files +=1
            target = folder / f'{file.parent.name}_{file.name}' 
            if file.resolve() != target.resolve():
                shutil.copy2(file, target)
            else:
                print(f"Skipped copying (same file): {file}")
            

    print(str(number_of_files) + ' files of type ' + file_type + ' found in ' + search_root)
