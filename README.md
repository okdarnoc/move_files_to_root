# Move_Files_To_Root

A Python script that recursively moves all files from subdirectories to a root folder. It provides multiple strategies for handling duplicate files and gives detailed operation statistics.

## Description

`move_files_to_root.py` is designed to help organize files by moving them from nested subdirectories to a single root directory. It offers various methods for handling duplicate files and provides clear feedback about the operation's progress and results.

## Features

- Moves files from any depth of subdirectories to the root folder
- Offers multiple duplicate handling strategies:
  - Skip existing files
  - Add counter to filename (e.g., document(1).pdf)
  - Add timestamp to filename
  - Overwrite existing files
  - Interactive mode with user prompts
- Provides operation statistics (files moved, skipped, errors)
- Includes comprehensive error handling

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/move_files_to_root.git
```

2. Navigate to the project directory:
```bash
cd move_files_to_root
```

## Usage

### Command Line

Run the script directly from the command line:
```bash
python move_files_to_root.py
```

The script will prompt you for:
- Root folder path
- Duplicate handling preference (in interactive mode)

### Python Import

```python
from move_files_to_root import move_files_to_root, DuplicateHandling

# Example with skip duplicates strategy
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.SKIP
)
```

### Duplicate Handling Options

```python
# Skip duplicates
success = move_files_to_root(duplicate_handling=DuplicateHandling.SKIP)

# Rename with counter
success = move_files_to_root(duplicate_handling=DuplicateHandling.RENAME_WITH_COUNTER)

# Rename with timestamp
success = move_files_to_root(duplicate_handling=DuplicateHandling.RENAME_WITH_TIMESTAMP)

# Overwrite existing files
success = move_files_to_root(duplicate_handling=DuplicateHandling.OVERWRITE)

# Interactive mode
success = move_files_to_root(duplicate_handling=DuplicateHandling.INTERACTIVE)
```

## Use Cases

### 1. Photography Organization
When consolidating photos from multiple cameras and events into a single directory:
```python
# Use timestamp for unique filenames
success = move_files_to_root(
    root_folder="/Users/username/Pictures/Vacation2023",
    duplicate_handling=DuplicateHandling.RENAME_WITH_TIMESTAMP
)
```

### 2. Downloads Cleanup
Organize a cluttered downloads folder with many subdirectories:
```python
# Interactive mode for careful file management
success = move_files_to_root(
    root_folder="/Users/username/Downloads",
    duplicate_handling=DuplicateHandling.INTERACTIVE
)
```

### 3. Project File Consolidation
Merge project files from multiple subfolders while preserving duplicates:
```python
# Use counter for duplicate files
success = move_files_to_root(
    root_folder="/path/to/project",
    duplicate_handling=DuplicateHandling.RENAME_WITH_COUNTER
)
```

### 4. Backup File Organization
Consolidate backup files while skipping existing ones:
```python
# Skip if file already exists
success = move_files_to_root(
    root_folder="/path/to/backups",
    duplicate_handling=DuplicateHandling.SKIP
)
```

### 5. Media Library Cleanup
Organize media files from various nested folders:
```python
# Overwrite older versions
success = move_files_to_root(
    root_folder="/path/to/media_library",
    duplicate_handling=DuplicateHandling.OVERWRITE
)
```

## Examples

### Interactive Mode Example
When running in interactive mode, you'll see prompts like this:
```
File 'document.pdf' already exists in destination.
Choose action:
[S]kip
[R]ename with counter
[T]imestamp rename
[O]verwrite
Your choice [S/R/T/O]: R

Moved: /path/to/subfolder/document.pdf -> /path/to/root/document(1).pdf

Operation completed:
Files moved: 15
Files skipped: 3
Errors encountered: 0
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
