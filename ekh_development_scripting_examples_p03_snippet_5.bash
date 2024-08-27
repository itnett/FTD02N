#!/bin/bash

THRESHOLD=80
PARTITION="/dev/sda1"

usage=$(df -h | grep $PARTITION | awk '{ print $5 }' | sed 's/%//g')

if [ $usage -gt $THRESHOLD ]; then
    echo "Disk usage for $PARTITION is at $usage%. Alert triggered!"
    # You can add email alerts or other notification mechanisms here
else
    echo "Disk usage for $PARTITION is under control."
fi