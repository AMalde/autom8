import os
from pathlib import Path
import shutil



def cleanFolder():
    folder_path = '/Users/aleksandermalde/downloads'
    os.chdir(folder_path)  # Changes the current working directory
    print("Current directory:", os.getcwd())

    files = os.listdir(folder_path)
    print(files)

def get_all_file_types_in_folder(folder: str, recursive: bool = False) -> list: 
    folder = Path(folder)
    if recursive:
        files = folder.rglob('*')
    else:
        files = folder.iterdir()

    extensions = {file.suffix.lower().lstrip('.') for file in files if file.is_file()}
    return list(extensions)

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
    #        if file.is_file():
            number_of_files +=1
            target = folder / f'{file.parent.name}_{file.name}' 
            if file.resolve() != target.resolve():
                shutil.copy2(file, target)
            else:
                print(f"Skipped copying (same file): {file}")
            

    print(str(number_of_files) + ' files of type ' + file_type + ' found in ' + search_root)
