#!/usr/bin/env bash

# Runs pytest and dumps stdout to a log file in the "res" directory

# Makes a date string to name the logs uniquely
datecode=$(date "+%Y%h%d_%H%M%S")

# Run pytest instruct it to make a Junit xml report, tee stdout to a log file
pytest -rapP --junitxml res/$datecode.xml | tee "res/$datecode.log"

# Generate a nice looking text report with xml2table
python xml2table.py res/$datecode.xml > "res/$datecode.report.txt"

# Show the test report to the user
cat res/$datecode.report.txt | less -S

# Show a message indicating where to see the report
clear
echo "Test report available at: res/$datecode.report.txt"
