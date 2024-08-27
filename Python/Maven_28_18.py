python
    def restore_database(backup_name, db_name):
        shutil.copyfile(backup_name, db_name)
        print(f"Gjenoppretting av database fullført: {db_name}")

    restore_database('organization_backup.db', 'organization_restored.db')