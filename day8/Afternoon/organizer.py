from pathlib import Path
import shutil

# Folder to organize
folder_path = Path(r"C:\Users\user\Downloads")

# Loop through every item in the folder
for item in folder_path.iterdir():

    # Skip directories (only organize files)
    if item.is_dir():
        continue

    # Get the file extension (e.g., '.pdf', '.jpg')
    extension = item.suffix.lower()

    # Ignore files without an extension
    if extension:

        # Create a folder named after the extension
        extension_folder = folder_path / extension[1:].upper()

        # Create the folder if it doesn't exist
        extension_folder.mkdir(exist_ok=True)

        # Move the file into the extension folder
        shutil.move(str(item), str(extension_folder / item.name))

print("Files have been organized successfully!")