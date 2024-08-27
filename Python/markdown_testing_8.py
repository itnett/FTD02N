python
import re
import os

def format_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expressions (same as PowerShell)
    formula_pattern = r'(?<!`)(\$\$)\s*(\\[.*?\\])\s*(\$\$)(?!`)'
    example_pattern = r'\s*([0-9a-zA-Z\+\-\*\/\^\(\)])\s*([0-9a-zA-Z\+\-\*\/\^\(\)])\s*'
    single_dollar_math_pattern = r'(?<!`)(\$)\s*(\(.*?\))\s*(\$)(?!`)'
    math_pattern = r'(?<!`)(\$?)(\s*[\(]*[0-9a-zA-Z\+\-\*\/\^\(\)\[\]\{\}]+[\)]*\s*)(\$?)(?!`)'

    # Replacement functions (same logic as PowerShell)
    def replace_formula(match):
        return match.group(1) + match.group(2) + match.group(3)

    def replace_example(match):
        return '$' + match.group(1) + match.group(2) + '$'

    def replace_single_dollar_math(match):
        return match.group(1) + match.group(2) + match.group(3)

    def replace_math(match):
        return '$' + match.group(2) + '$'

    # Apply replacements sequentially, avoiding code blocks
    new_content = content
    for line in content.splitlines():
        if not line.startswith('