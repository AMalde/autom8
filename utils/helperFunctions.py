import os
from pathlib import Path
import shutil



def get_all_file_types_in_folder(folder: str, recursive: bool = False) -> list: 
    folder = Path(folder)
    if recursive:
        files = folder.rglob('*')
    else:
        files = folder.iterdir()

    extensions = {file.suffix.lower().lstrip('.') for file in files if file.is_file()}
    return list(extensions)


#def createFolder(folder_name, location): 
