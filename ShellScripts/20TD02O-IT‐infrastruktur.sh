bash
  #!/bin/bash
  config_dir="/etc/config"
  backup_dir="/backup/config"
  date=$(date +%Y-%m-%d)
  tar -czvf "$backup_dir/config-backup-$date.tar.gz" "$config_dir"
  echo "Sikkerhetskopiering fullført: $backup_dir/config-backup-$date.tar.gz"