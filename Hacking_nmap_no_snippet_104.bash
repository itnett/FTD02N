#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

# Compile the Java code
javac scans/IntelligentScan.java

# Run the Java program
java -cp scans IntelligentScan $target