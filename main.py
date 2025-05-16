from utils.cleanDownloads import cleanFolder
from utils.cleanDownloads import organiseFiles
from utils.cleanDownloads import get_all_file_types_in_folder



downloadFolder = '/Users/aleksandermalde/downloads'

def main():
    print("Welcome\n")
    exts = get_all_file_types_in_folder(downloadFolder, recursive=True)

    for ext in exts:
        print(f"Found file type: {ext}")
        organiseFiles(downloadFolder, ext)
    #organiseFiles(downloadFolder, "docx")
    #organiseFiles(downloadFolder, "jpg")



if __name__ == "__main__":
    main()