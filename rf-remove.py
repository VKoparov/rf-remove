#!/usr/bin/env python3

import os
import sys

def delete_file(filename, exclude_dirs, directory):
    deleted_files_count = 0
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                deleted_files_count += 1
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
    
    return deleted_files_count

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <filename> [exclude_dir1 exclude_dir2 ...] <directory>")
        sys.exit(1)

    file_to_delete = sys.argv[1]
    exclude_dirs = sys.argv[2:-1]
    directory_to_search = sys.argv[-1]

    if not os.path.isdir(directory_to_search):
        print(f"Error: '{directory_to_search}' is not a valid directory.")
        sys.exit(1)

    exclude_dirs = [os.path.abspath(d) for d in exclude_dirs]

    deleted_count = delete_file(file_to_delete, exclude_dirs, directory_to_search)

    if deleted_count > 0:
        print(f"Deleted {deleted_count} file(s).")
    else:
        print(f"No files named '{file_to_delete}' found in {directory_to_search}.")

