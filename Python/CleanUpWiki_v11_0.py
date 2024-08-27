python
import os
import re
import subprocess
import datetime
import yaml

# Last inn konfigurasjonen fra input.yml
with open('input.yml', 'r') as file:
    config = yaml.safe_load(file)

wiki_repo_url = config['wiki_repo_url']
dump_directory = config['dump_directory']
code_repo_url = config['code_repo_url']
wiki_repo_new_url = config['wiki_repo_new_url']
code_repo_directory = config['code_repo_directory']
wiki_repo_directory = config['wiki_repo_directory']

# Funksjon for å sjekke om en katalog er et git-repo
def is_git_repo(directory):
    return os.path.isdir(os.path.join(directory, '.git'))

# Funksjon for å sikre at katalogen er et Git-repo (kloner hvis nødvendig)
def ensure_git_repo(directory, repo_url):
    if not is_git_repo(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        subprocess.run(["git", "clone", repo_url, directory])
    os.chdir(directory)

# Funksjon for å identifisere kjørbar kode i et kjent format
def is_executable_code_block(code_block):
    executable_patterns = [r'^