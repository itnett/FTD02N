python
import os
import re
import shutil
import subprocess
import yaml
from datetime import datetime

def load_input_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        print(f"Loaded configuration from {file_path}")
        return config
    except Exception as e:
        log(f"Error loading configuration: {e}")
        raise

def clone_wiki_repo(wiki_repo_url, target_directory):
    try:
        if os.path.exists(target_directory):
            shutil.rmtree(target_directory)
        os.makedirs(target_directory)
        subprocess.run(["git", "clone", wiki_repo_url, target_directory], check=True)
        print(f"Cloned Wiki repository to {target_directory}")
    except subprocess.CalledProcessError as e:
        log(f"Error cloning repository: {e}")
        raise
    except Exception as e:
        log(f"General error during cloning: {e}")
        raise

def process_wiki_files(wiki_dir, code_repo_url, code_repo_dir):
    try:
        for root, dirs, files in os.walk(wiki_dir):
            for file in files:
                if file.endswith(".md"):
                    wiki_filepath = os.path.join(root, file)
                    with open(wiki_filepath, 'r') as f:
                        content = f.read()

                    code_blocks = re.findall(r'