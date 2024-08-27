#!/bin/bash

threshold=80  # Terskelverdi for diskbruk i prosent

usage=$(df -h | awk '$NF=="/"{printf "%d", $5}')

if [ "$usage" -gt "$threshold" ]; then
    echo "Diskbruken er over $threshold%!"
    # Send varsel via e-post eller annen metode


fi