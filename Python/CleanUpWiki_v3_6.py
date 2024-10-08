python
import os
import yaml
import shutil
from zipfile import ZipFile
from datetime import datetime

def load_input_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def backup_and_recreate_directory(directory_path):
    if os.path.exists(directory_path) and os.listdir(directory_path):
        # Lag zip-fil med dagens dato og tid i navnet
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_zip = f"{directory_path}_{timestamp}.zip"
        
        with ZipFile(backup_zip, 'w') as zipf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))
        
        print(f"Backup of {directory_path} created at {backup_zip}")
        
        # Slett den eksisterende katalogen
        shutil.rmtree(directory_path)
        print(f"Deleted the directory: {directory_path}")
    
    # Opprett katalogen på nytt
    os.makedirs(directory_path, exist_ok=True)
    print(f"Created new directory: {directory_path}")

def main():
    try:
        config = load_input_config("input.yml")
        
        # Sjekk og backup/rekreasjon av katalogene fra input.yml
        directories = [config['dump_directory'], config['code_repo_directory']]
        
        for directory in directories:
            backup_and_recreate_directory(directory)
        
        print("All directories have been backed up (if needed) and recreated.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()