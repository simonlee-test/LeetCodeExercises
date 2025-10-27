import re
import os


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename to make it safe for file system operations.

    Args:
        filename: The input filename to sanitize

    Returns:
        A sanitized filename that is safe to use
    """
    if not filename:
        raise ValueError("Filename cannot be empty")

    # Remove or replace characters that are invalid in filenames
    # Invalid characters: < > : " / \ | ? * and control characters
    invalid_chars = r'[>"\/|?*\x00-\x1f]'
    sanitized = re.sub(invalid_chars, "_", filename)

    # Remove leading and trailing whitespace and dots
    sanitized = sanitized.strip(". ")

    # Ensure filename is not empty after sanitization
    if not sanitized:
        sanitized = "unnamed_file"

    # Limit filename length (typically 255 characters max for most filesystems)
    max_length = 255
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]

    # Remove consecutive underscores
    sanitized = re.sub(r"_+", "_", sanitized)

    return sanitized


def create_python_file(content: str, filename: str = None) -> str:
    """
    Create a new Python file with sanitized filename.

    Args:
        content: The Python code content to write to the file
        filename: Optional filename. If None, will prompt user for input

    Returns:
        The path to the created file
    """
    if filename is None:
        filename = input("Enter filename for the new Python file: ")

    # Sanitize the filename
    safe_filename = sanitize_filename(filename)

    # Ensure filename ends with .py
    if not safe_filename.endswith(".py"):
        safe_filename += ".py"

    # Check if file already exists
    if os.path.exists(safe_filename):
        counter = 1
        base_name = safe_filename[:-3]  # Remove .py extension
        while os.path.exists(f"{base_name}_{counter}.py"):
            counter += 1
        safe_filename = f"{base_name}_{counter}.py"

    try:
        with open(safe_filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully created file: {safe_filename}")
        return safe_filename
    except Exception as e:
        print(f"Error creating file: {e}")
        raise


if __name__ == "__main__":
    # Create an empty Python file with user input
    try:
        created_file = create_python_file("")
        print(f"Created empty file: {created_file}")
    except Exception as e:
        print(f"Error creating file: {e}")
