# Delete Duplicates Script

This script is designed to delete duplicate image files (with extensions `.jpg`, `.jpeg`, `.png`, `.svg`, `.heic`, `.heif`) within a specified folder and its subfolders (if requested).

## Prerequisites

- Python 3.x installed on your machine.
- Modules `os`, `re`, `tkinter`, and `filedialog` installed.

## Usage

1. Clone or download the repository to your machine.
2. Open a command prompt or terminal window in the directory where the script file is saved.
3. Enter the following command: `python delete_duplicates.py`
4. The script will open a file dialog box. Select the folder that contains the images you want to check for duplicates.
5. The script will prompt you to indicate if you would like to delete duplicates in subfolders too. Enter `0` for No or `1` for Yes.
6. The script will search for duplicate images and delete them. The script will print the paths of the deleted files to the console.

Note: Be careful when running this script, as it will permanently delete files from your system. Make sure to select the correct folder and confirm your decision to delete duplicates in subfolders.
