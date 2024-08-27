#!/bin/bash
  source_dir="/path/to/source"
  backup_dir="/path/to/backup"
  date=$(date +%Y-%m-%d)
  tar -czvf "$backup_dir/backup-$date.tar.gz" "$source_dir"
  echo "Sikkerhetskopi fullført: $backup_dir/backup-$date.tar.gz"