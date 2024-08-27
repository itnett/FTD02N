python
# Load the contents of the file to extract flowcharts
file_path = '/mnt/data/SC‐200_flashcards_v4.md'
with open(file_path, 'r') as file:
    content = file.read()

# Displaying the content for inspection
content[:5000]  # Displaying the first 5000 characters for inspection