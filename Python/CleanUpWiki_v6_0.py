python
import os
import re
import shutil
import subprocess
import yaml
import logging
import traceback
from datetime import datetime
import stat

# Setup logging
logging.basicConfig(filename="C:\\WikiMigration\\migration.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log(message):
    logging.info(message)
    print(message)

def log_exception(e):
    log(f"Exception occurred: {str(e)}")
    log(traceback.format_exc())

def load_input_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        validate_config(config)
        log(f"Loaded configuration from {file_path}")
        return config
    except Exception as e:
        log_exception(e)
        raise

def validate_config(config):
    required_keys = ['wiki_repo_url', 'dump_directory', 'code_repo_url', 'code_repo_directory']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")
        if not config[key]:
            raise ValueError(f"Config key {key} cannot be empty.")
    log("Configuration validated successfully.")

def handle_remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def run_git_command(commands, cwd):
    result = subprocess.run(commands, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        log(f"Git command failed: {' '.join(commands)}")
        log(f"stdout: {result.stdout}")
        log(f"stderr: {result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, commands)
    return result.stdout

def sanitize_filename(filename):
    # Fjern eller erstatt tegn som ikke er tillatt i Windows-filnavn
    return re.sub(r'[<>:"/\\|?*&]', '_', filename)

def clone_wiki_repo(wiki_repo_url, target_directory):
    try:
        if os.path.exists(target_directory):
            shutil.rmtree(target_directory, onerror=handle_remove_readonly)
        os.makedirs(target_directory)
        run_git_command(["git", "clone", wiki_repo_url, target_directory], cwd=target_directory)
        log(f"Cloned Wiki repository to {target_directory}")
    except Exception as e:
        log_exception(e)
        raise

def process_wiki_files(wiki_dir, code_repo_url, code_repo_dir):
    try:
        for root, dirs, files in os.walk(wiki_dir):
            for file in files:
                if file.endswith(".md"):
                    wiki_filepath = os.path.join(root, file)
                    with open(wiki_filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    code_blocks = re.findall(r'