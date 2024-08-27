python
import re

log_file = 'auth.log'
pattern = r'Failed password for invalid user'

with open(log_file, 'r') as f:
    for line in f:
        if re.search(pattern, line):
            print(line.strip())