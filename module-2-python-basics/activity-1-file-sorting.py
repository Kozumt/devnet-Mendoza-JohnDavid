"""
Module 2 — Activity: File Sorting with os and shutil
Student: John David Mendoza
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I build a Python program that organizes files into folders.
The Python program checks the file extension and moves JPG and PNG files into the Images folder. The Python program also moves PDF and DOCX files into the Documents folder.



============================================
KEY VOCABULARY
============================================
- os module: Os module helps me to work with files and folders.
- shutil module: Shutil module helps me to move and manage files.
- file path: File path is the location of a file or folder.
- directory: Directory is another name for a folder.
- file extension: Is the part, at the end of file name that shows its type


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder = "my_files"

for file in os.listdir(folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(
            os.path.join(folder, file),
            os.path.join(folder, "Images", file)
        )
        elif file.endswith(".pdf") or file.endswith(".docx"):
        shutil.move(
            os.path.join(folder, file),
            os.path.join(folder, "Documents", file)
        )

print("File Organized")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
The mistake that I did and want to avoid is using the wrong folder path. If the folder does not exist, the program gives error.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

"""
