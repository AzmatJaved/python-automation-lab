import os
from datetime import datetime

source_folder = "/Users/azmat/Documents/Arabic101"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        timestamp = os.path.getmtime(file_path)
        date_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d_%H-%M-%S")
        new_file_name = f"{date_time}_{file}"
        new_file_path = os.path.join(source_folder, new_file_name)

        # Handle duplicate file names
        if os.path.exists(new_file_path):
            base, ext = os.path.splitext(new_file_name)
            new_file_path = os.path.join(source_folder, f"{base}_copy{ext}")

        os.rename(file_path, new_file_path)

print("✅ Files renamed successfully!")