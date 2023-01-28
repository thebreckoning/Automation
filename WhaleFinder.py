#The purpose of this script is to help me clean up my hard drive by finding all the large files so I can review and delete anything I don't need.

import os
import csv
import mimetypes

# Set the threshold for file size (in bytes)
threshold = 5 * 1024 * 1024 * 1024

# Create a folder to save the csv
if not os.path.exists("Whales"):
    os.mkdir("Whales")

# Open a CSV file for writing
with open('Whales/Whales.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'File Size (GB)', 'File Type', 'File Location'])

    # Walk through all the files and directories on the entire computer
    for dirpath, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            # Get the full file path
            file_path = os.path.join(dirpath, filename)

            # Check the file size
            if os.path.getsize(file_path) > threshold:
                # Get the file type using mimetypes library
                file_type, encoding = mimetypes.guess_type(file_path)
                # Get the file size in GB
                file_size = os.path.getsize(file_path) / (1024 * 1024 * 1024)
                # Write the file information to the CSV file
                writer.writerow([filename, file_size, file_type, file_path])
