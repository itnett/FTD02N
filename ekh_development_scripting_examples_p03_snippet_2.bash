#!/bin/bash

SOURCE_DIR="/home/user/data"
DEST_DIR="/backup/user/data"
REMOTE_SERVER="backup.example.com"
REMOTE_USER="backupuser"

rsync -avz --delete $SOURCE_DIR $REMOTE_USER@$REMOTE_SERVER:$DEST_DIR

if [ $? -eq 0 ]; then
    echo "Backup successful!"
else
    echo "Backup failed!"
fi