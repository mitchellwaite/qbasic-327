#!/usr/bin/env bash

# Runs pytest and dumps stdout to a log file in the "res" directory

datecode=$(date "+%Y%h%d_%H%M%S")

pytest -rapP --junitxml res/$datecode.xml | tee "res/$datecode.log"

python xml2table.py res/$datecode.xml > "res/$datecode.report.txt"

cat res/$datecode.report.txt | less -S

clear

echo "Test report available at: res/$datecode.report.txt"
