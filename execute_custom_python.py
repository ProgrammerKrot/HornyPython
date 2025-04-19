import sys
import os
from my_python_config import CUSTOM_SYNTAX_REVERSE  # Maps your syntax → Python


def restore_python_code(custom_code):
    """Converts your custom syntax back to valid Python."""
    # Sort keys by length (longest first) to avoid partial replacements
    sorted_replacements = sorted(
        CUSTOM_SYNTAX_REVERSE.items(),
        key=lambda x: -len(x[0])
    )
    for custom, original in sorted_replacements:
        # Use regex to match whole words only
        custom_code = re.sub(
            r'\b' + re.escape(custom) + r'\b',
            original,
            custom_code
        )
    return custom_code


def execute_transformed_file(file_path):
    """Reads a file with custom syntax, restores it to Python, and executes it."""
    with open(file_path, 'r') as f:
        custom_code = f.read()

    python_code = restore_python_code(custom_code)

    # Execute the restored Python code
    exec_globals = {}
    exec(python_code, exec_globals)
    return exec_globals


if __name__ == "__main__":
    import re  # Import here to avoid revealing it in the transformed code

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <transformed_file>")
        sys.exit(1)

    file_to_run = sys.argv[1]
    if not os.path.exists(file_to_run):
        print(f"Error: File '{file_to_run}' not found.")
        sys.exit(1)

    execute_transformed_file(file_to_run)