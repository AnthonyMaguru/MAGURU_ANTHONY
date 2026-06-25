import os
import shutil

folder_path = r"C:\Users\user\Downloads" 

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get extension
    extension = os.path.splitext(file)[1].lower()

    if extension:
        # Create folder with extension name
        ext_folder = os.path.join(folder_path, extension[1:].upper())

        if not os.path.exists(ext_folder):
            os.mkdir(ext_folder)

        # Move file
        shutil.move(file_path, os.path.join(ext_folder, file))