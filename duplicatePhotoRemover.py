import os
import re
from tkinter import filedialog, Tk

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.svg', '.heic', '.heif']

def delete_duplicates(path, check_subfolders=False):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if any(filename.lower().endswith(extension) for extension in IMAGE_EXTENSIONS) and re.search(r"\(\d+\)", filename) or "- Copy" in filename:
                os.remove(os.path.join(dirpath, filename))
                print(f"Deleted {os.path.join(dirpath, filename)}")
        if not check_subfolders:
            dirnames.clear()

def main():
    root = Tk()
    root.withdraw() 
    path = filedialog.askdirectory()
    
    check_subfolders = int(input("Would you like to remove duplicates in subfolders too?\nEnter 0 for No or 1 for Yes: "))
    delete_duplicates(path, check_subfolders)

if __name__ == "__main__":
    main()
