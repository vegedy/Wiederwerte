import kagglehub
import os

# Download the dataset
path = kagglehub.dataset_download("mostafaabla/garbage-classification")
print("Path to dataset files:", path)

# List all directories in the dataset and count the total number of files
file_count = 0
for root, dirs, files in os.walk(path):
    if len(dirs) > 1:
        print("Classes:", dirs)
    file_count += len(files)

print("Total files:", file_count)
