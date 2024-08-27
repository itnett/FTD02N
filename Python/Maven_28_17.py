python
    import shutil

    def backup_database(db_name, backup_name):
        shutil.copyfile(db_name, backup_name)
        print(f"Backup av database fullført: {backup_name}")

    backup_database('organization.db', 'organization_backup.db')