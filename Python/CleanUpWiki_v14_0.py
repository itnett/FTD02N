python
import os
import re
import subprocess
import datetime
import yaml

# Last inn konfigurasjoner fra input.yml
with open("input.yml", 'r') as stream:
    config = yaml.safe_load(stream)

wiki_repo_url = config['wiki_repo_url']
dump_directory = config['dump_directory']
code_repo_url = config['code_repo_url']
code_repo_directory = config['code_repo_directory']

# Funksjon for å identifisere kjørbar kode i et kjent format
def is_executable_code_block(code_block):
    executable_patterns = [r'^