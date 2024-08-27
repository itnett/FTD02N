python
import os
import shutil
from zipfile import ZipFile
from datetime import datetime
import stat
import traceback
import logging
import yaml

# Setup logging
logging.basicConfig(filename="C:\\WikiMigration\\backup_prepare.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log(message):
    logging.info(message)
    print(message)

def log_exception(e):
    logging.error(f"Exception occurred: {str(e)}")
    logging.error(traceback.format_exc())

def load_input_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        log_exception(e)
        raise

def handle_remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def backup_and_recreate_directory(directory_path):
    try:
        if os.path.exists(directory_path) and os.listdir(directory_path):
            # Lag zip-fil med dagens dato og tid i navnet
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_zip = f"{directory_path}_{timestamp}.zip"
            
            with ZipFile(backup_zip, 'w') as zipf:
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, directory_path))
            
            log(f"Backup of {directory_path} created at {backup_zip}")
            
            # Slett den eksisterende katalogen
            shutil.rmtree(directory_path, onerror=handle_remove_readonly)
            log(f"Deleted the directory: {directory_path}")
        
        # Opprett katalogen på nytt
        os.makedirs(directory_path, exist_ok=True)
        log(f"Created new directory: {directory_path}")
    except Exception as e:
        log_exception(e)
        raise

def main():
    try:
        config = load_input_config("input.yml")
        
        # Sjekk og backup/rekreasjon av katalogene fra input.yml
        directories = [config['dump_directory'], config['code_repo_directory']]
        
        for directory in directories:
            backup_and_recreate_directory(directory)
        
        log("All directories have been backed up (if needed) and recreated.")
    
    except Exception as e:
        log_exception(e)
        print("An error occurred, please check the log file for details.")

if __name__ == "__main__":
    main()