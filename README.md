# Move Files to Root

A Python utility script that recursively moves all files from subdirectories to a root folder with configurable duplicate handling strategies.

## Features

- Move files from nested subdirectories to a root folder
- Multiple duplicate handling strategies:
  - Skip existing files
  - Rename with counter (e.g., file(1).txt)
  - Rename with timestamp
  - Overwrite existing files
  - Interactive mode with user prompts
- Detailed operation statistics
- Error handling and reporting

## Installation

Clone this repository and ensure you have Python 3.6 or higher installed.

```bash
git clone <repository-url>
cd <repository-name>
```

## Usage

### Basic Usage

```python
from move_files_to_root import move_files_to_root, DuplicateHandling

# Move files with default settings (skip duplicates)
success = move_files_to_root("/path/to/root/folder")
```

### Duplicate Handling Strategies

```python
# Skip duplicates (default behavior)
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.SKIP
)

# Rename duplicates with counter
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.RENAME_WITH_COUNTER
)

# Rename duplicates with timestamp
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.RENAME_WITH_TIMESTAMP
)

# Overwrite existing files
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.OVERWRITE
)

# Interactive mode (prompts user for each duplicate)
success = move_files_to_root(
    root_folder="/path/to/folder",
    duplicate_handling=DuplicateHandling.INTERACTIVE
)
```

### Command Line Usage

Run the script directly from the command line:

```bash
python move_files_to_root.py
```

## Example Use Cases

### 1. Consolidating Downloaded Files

If you have a Downloads folder with nested subdirectories and want to move all files to the root Downloads folder:

```python
from move_files_to_root import move_files_to_root, DuplicateHandling

# Move files with timestamp renaming for duplicates
success = move_files_to_root(
    root_folder="/Users/username/Downloads",
    duplicate_handling=DuplicateHandling.RENAME_WITH_TIMESTAMP
)
```

### 2. Photo Organization

When organizing photos that might have duplicate names from different cameras:

```python
# Interactive mode for careful photo organization
success = move_files_to_root(
    root_folder="/Users/username/Pictures/Vacation2023",
    duplicate_handling=DuplicateHandling.INTERACTIVE
)
```

### 3. Project File Consolidation

When consolidating project files while ensuring no files are accidentally overwritten:

```python
# Use counter for duplicate files
success = move_files_to_root(
    root_folder="/path/to/project",
    duplicate_handling=DuplicateHandling.RENAME_WITH_COUNTER
)
```

## Sample Output

When running in interactive mode:

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

## Error Handling

The script handles various error scenarios:
- Invalid or non-existent paths
- Permission issues
- File system errors
- Duplicate file conflicts

## Return Values

- Returns `True` if all operations completed successfully
- Returns `False` if any errors were encountered
- Exit code 0 for success, 1 for failure when run as main script

## Requirements

- Python 3.6+
- Standard library modules only (no external dependencies)
