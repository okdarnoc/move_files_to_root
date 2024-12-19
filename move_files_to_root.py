import os
import shutil
from datetime import datetime
from typing import Optional, Literal
from enum import Enum

class DuplicateHandling(Enum):
    """Enumeration of different strategies for handling duplicate files"""
    SKIP = "skip"              # Skip if duplicate exists
    RENAME_WITH_COUNTER = "counter"    # Add number suffix
    RENAME_WITH_TIMESTAMP = "timestamp"  # Add timestamp
    OVERWRITE = "overwrite"    # Replace existing file
    INTERACTIVE = "interactive"  # Ask user what to do

def generate_unique_filename(base_path: str, duplicate_handling: DuplicateHandling) -> str:
    """
    Generate a unique filename based on the chosen duplicate handling strategy.
    
    Args:
        base_path: Original file path
        duplicate_handling: Strategy to handle duplicates
    
    Returns:
        str: New unique file path
    """
    # Split the file path into directory, name, and extension
    directory = os.path.dirname(base_path)
    filename = os.path.basename(base_path)
    name, ext = os.path.splitext(filename)
    
    if duplicate_handling == DuplicateHandling.RENAME_WITH_COUNTER:
        # Try increasing numbers until we find a unique filename
        counter = 1
        while os.path.exists(base_path):
            new_name = f"{name}({counter}){ext}"
            base_path = os.path.join(directory, new_name)
            counter += 1
            
    elif duplicate_handling == DuplicateHandling.RENAME_WITH_TIMESTAMP:
        # Add timestamp to filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{name}_{timestamp}{ext}"
        base_path = os.path.join(directory, new_name)
        
    return base_path

def handle_duplicate_interactive(file: str, dest_path: str) -> str:
    """
    Interactively handle duplicate files by asking user for action.
    
    Args:
        file: Name of the file being processed
        dest_path: Destination path where duplicate exists
    
    Returns:
        str: Path where file should be moved, or None to skip
    """
    while True:
        action = input(f"\nFile '{file}' already exists in destination.\n"
                      f"Choose action:\n"
                      f"[S]kip\n"
                      f"[R]ename with counter\n"
                      f"[T]imestamp rename\n"
                      f"[O]verwrite\n"
                      f"Your choice [S/R/T/O]: ").strip().upper()
        
        if action == 'S':
            return None
        elif action == 'R':
            return generate_unique_filename(dest_path, DuplicateHandling.RENAME_WITH_COUNTER)
        elif action == 'T':
            return generate_unique_filename(dest_path, DuplicateHandling.RENAME_WITH_TIMESTAMP)
        elif action == 'O':
            return dest_path
        else:
            print("Invalid choice. Please try again.")

def move_files_to_root(
    root_folder: Optional[str] = None,
    duplicate_handling: DuplicateHandling = DuplicateHandling.SKIP
) -> bool:
    """
    Moves all files from subdirectories to the root folder with specified duplicate handling.
    
    Args:
        root_folder: Path to root folder. If None, will prompt user for input.
        duplicate_handling: Strategy for handling duplicate files
        
    Returns:
        bool: True if operation was successful, False otherwise
    """
    # Get and validate root folder path
    if root_folder is None:
        root_folder = input("Enter the absolute path to the root folder: ").strip()
    
    # Convert to absolute path and validate
    try:
        root_folder = os.path.abspath(root_folder)
        if not os.path.exists(root_folder):
            print(f"Error: The folder '{root_folder}' does not exist.")
            return False
        if not os.path.isdir(root_folder):
            print(f"Error: The path '{root_folder}' is not a directory.")
            return False
    except Exception as e:
        print(f"Error validating path: {str(e)}")
        return False

    # Initialize counters for operation statistics
    files_moved = 0
    files_skipped = 0
    errors = 0

    try:
        # Walk through directory tree bottom-up to safely move files
        for dirpath, dirnames, filenames in os.walk(root_folder, topdown=False):
            # Skip root directory to avoid reprocessing
            if dirpath == root_folder:
                continue

            # Process each file in current directory
            for file in filenames:
                source_path = os.path.join(dirpath, file)
                dest_path = os.path.join(root_folder, file)

                try:
                    # Handle case where destination file already exists
                    if os.path.exists(dest_path):
                        if duplicate_handling == DuplicateHandling.SKIP:
                            print(f"Warning: File '{file}' already exists in root folder. Skipping.")
                            files_skipped += 1
                            continue
                            
                        elif duplicate_handling == DuplicateHandling.INTERACTIVE:
                            new_dest = handle_duplicate_interactive(file, dest_path)
                            if new_dest is None:
                                files_skipped += 1
                                continue
                            dest_path = new_dest
                            
                        elif duplicate_handling in (DuplicateHandling.RENAME_WITH_COUNTER, 
                                                 DuplicateHandling.RENAME_WITH_TIMESTAMP):
                            dest_path = generate_unique_filename(dest_path, duplicate_handling)
                            
                        # OVERWRITE case uses original dest_path

                    # Move the file to destination
                    shutil.move(source_path, dest_path)
                    print(f"Moved: {source_path} -> {dest_path}")
                    files_moved += 1

                except (OSError, shutil.Error) as e:
                    print(f"Error moving file '{file}': {str(e)}")
                    errors += 1

        # Print operation summary
        print("\nOperation completed:")
        print(f"Files moved: {files_moved}")
        print(f"Files skipped: {files_skipped}")
        print(f"Errors encountered: {errors}")

        return errors == 0

    except Exception as e:
        print(f"Fatal error: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage with different duplicate handling strategies
    
    # To skip duplicates (default behavior):
    # success = move_files_to_root(duplicate_handling=DuplicateHandling.SKIP)
    
    # To rename with counter:
    # success = move_files_to_root(duplicate_handling=DuplicateHandling.RENAME_WITH_COUNTER)
    
    # To rename with timestamp:
    # success = move_files_to_root(duplicate_handling=DuplicateHandling.RENAME_WITH_TIMESTAMP)
    
    # To overwrite existing files:
    # success = move_files_to_root(duplicate_handling=DuplicateHandling.OVERWRITE)
    
    # To handle duplicates interactively:
    success = move_files_to_root(duplicate_handling=DuplicateHandling.INTERACTIVE)
    
    # Exit with appropriate status code
    exit(0 if success else 1)
