python
# Bruke buffer for effektiv lesing av store filer
with open('large_file.txt', 'r') as file:
    while chunk := file.read(8192):
        process(chunk)