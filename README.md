Search for and delete all occurrences of a file in the given directory and its subdirectories,excluding specific directories.

Configuration:
  - terminal: add ***alias <alias name>="/<prefered lcoation (absolute path)>/rf-remove.py"*** to zshrc/bashrc config.

Parameters:
  - filename (str): The name of the file to search for and delete.
  - exclude_dirs (list): List of directories to exclude from the search.
  - directory (str): The root directory where the search starts.

Returns:
  - int: The number of files deleted.

Usage:
  - command: rf-remove<alias name> .DS_Store /Users/Shared/Desktop 
