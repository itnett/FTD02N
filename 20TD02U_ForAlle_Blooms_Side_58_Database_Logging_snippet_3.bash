#!/bin/bash

# Enkelt script for å overvåke feilloggen i sanntid
tail -f /var/log/mysql/error.log | while read LINE
do
    echo "ERROR DETECTED: $LINE"
done