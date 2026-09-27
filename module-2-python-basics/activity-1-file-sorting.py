"""
Module 2 — Activity: File Sorting with os and shutil
Student: John David Mendoza
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


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
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
