python
import os
import re
import shutil
import subprocess
import yaml
from datetime import datetime

# Funksjon for å lese inputfilen
def load_input_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Funksjon for å klone Wiki-repoet
def clone_wiki_repo(wiki_repo_url, target_directory):
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)
    os.makedirs(target_directory)
    subprocess.run(["git", "clone", wiki_repo_url, target_directory])
    print(f"Cloned Wiki repository to {target_directory}")

# Funksjon for å ekstrahere kodeblokker og erstatte med lenker
def process_wiki_files(wiki_dir, code_repo_url, code_repo_dir):
    for root, dirs, files in os.walk(wiki_dir):
        for file in files:
            if file.endswith(".md"):
                wiki_filepath = os.path.join(root, file)
                with open(wiki_filepath, 'r') as f:
                    content = f.read()

                # Finn og ekstraher kodeblokker
                code_blocks = re.findall(r'