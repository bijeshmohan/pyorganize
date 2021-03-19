import os
from pathlib import Path
from sys import argv

# Directory to File extensions
dir_to_extns = {
    "Audios": ["wav", "mp3", "wma", "aac"],
    "Images": ["jpg", "jpeg", "bmp", "png", "gif", "tiff"],
    "Videos": ["mp4", "mpeg4", "mkv", "avi", "wmv", "flv"],
    "Documents": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "ods", "txt", "csv", "tsv"],
    "Codes": ["py", "c", "cpp", "js"],
    "Applications": ["exe", "msi", "deb", "rpm"]
}

if len(argv) != 2:
    if os.name == "nt":
        print("[ERROR] Usage: python organize.py C:\path\to\directory")
    else:
        print("[ERROR] Usage: python organize.py /path/to/directory")
    exit(1)

# Source directory which needs to be organized
src = Path(argv[1])

if not src.exists():
    print(f"[ERROR]: '{src}' does NOT exist!")
    exit(1)

if not src.is_dir():
    print(f"[ERROR]: '{src}' is NOT a directory!")
    exit(1)

# Files in source directory
files = [item for item in src.iterdir() if item.is_file()]

# Create Directory to Files dictionary
dir_to_files = {}
for directory, extensions in dir_to_extns.items():
    dir_to_files[directory] = [file for file in files if file.suffix[1:].lower() in extensions]

# Organize source directory
for directory, files in dir_to_files.items():
    dst = src / directory  # destination
    for file in files:
        if not dst.is_dir():
            dst.mkdir()
        file.rename(dst / file.name)
