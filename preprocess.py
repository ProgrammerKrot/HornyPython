import re
from my_python_config import CUSTOM_SYNTAX


def preprocess_code(input_file, output_file):
    """
    Reads a Python file, replaces keywords based on CUSTOM_SYNTAX,
    and writes the transformed code to a new file.
    """
    with open(input_file, 'r') as f:
        code = f.read()

    # Sort keys by length (longest first) to avoid partial replacements
    sorted_replacements = sorted(
        CUSTOM_SYNTAX.items(),
        key=lambda x: -len(x[0]))

    for original, custom in sorted_replacements:
    # Use regex to match whole words only
        code = re.sub(r'\b' + re.escape(original) + r'\b', custom, code)

    with open(output_file, 'w') as f:
        f.write(code)

if __name__ == "__main__":
    input_file = "Example.py"  # Your original Python file
    output_file = "Example.hornypy"  # Output file with custom syntax
    preprocess_code(input_file, output_file)