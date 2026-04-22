import os
import shutil

source_folder = "/Users/azmat/Documents/Arabic101"
print("os.listdir", os.listdir(source_folder))
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        if file.endswith((".jpg", ".png")):
            folder = "Images"
        elif file.endswith((".pdf", ".docx")):
            folder = "Documents"
        elif file.endswith(".mp4"):
            folder = "Videos"   
        elif file.endswith(".zip"):
            folder = "Archives"
        else:
            folder = "Others"

        dest_folder = os.path.join(source_folder, folder)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        dest_path = os.path.join(dest_folder, file)

        # Handle duplicate file names
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(file)
            dest_path = os.path.join(dest_folder, f"{base}_copy{ext}")

        shutil.move(file_path, dest_path)