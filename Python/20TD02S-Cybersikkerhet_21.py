python
import re

log_file = 'server.log'
pattern = r'ERROR'

with open(log_file, 'r') as file:
    for line in file:
        if re.search(pattern, line):
            print(line.strip())