python
import os
import re
import subprocess
import datetime
import yaml

# Laster inn konfigureringen fra input.yml
with open("input.yml", "r") as file:
    config = yaml.safe_load(file)

wiki_repo_url = config['wiki_repo_url']
dump_directory = config['dump_directory']
code_repo_directory = config['code_repo_directory']
code_repo_url = config['code_repo_url']

# Funksjon for å identifisere kjørbar kode i et kjent format
def is_executable_code_block(code_block):
    executable_patterns = [r'^