#!C:\Users\bucky\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11\Python 3.11 (64-bit).lnk

import os
import csv
import mimetypes

# Set the threshold for file size (in bytes)
threshold = 10 * 1024 * 1024 * 1024

# Create a folder to save the csv
if not os.path.exists("Whales"):
    os.mkdir("Whales")

# Open a CSV file for writing
with open('Whales/Whales.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Type', 'File Size (GB)', 'File Name', 'File Location'])

    # Walk through all the files and directories in the C drive
    for dirpath, dirnames, filenames in os.walk('C:\\'):
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
                writer.writerow([file_type, file_size, filename, file_path])
