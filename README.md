# qbasic-327

## Build Status

[![Build Status](https://travis-ci.org/mitchellwaite/qbasic-327.svg?branch=master)](https://travis-ci.org/mitchellwaite/qbasic-327)

## About

A (horribly designed) bank/transaction management software used as an educational exercise in CISC 327 (Software Quality Assurance) at Queen's University

## Prerequisites

- UNIX like operating system. I have tested on Mac OS X only, but Linux or Bash on windows 10 should theoretically work
- A version of Python 2.7
- PIP packages installed. Use the following command from this directory: `pip install -r requirements.txt`

### Running the Front End

Change to the src/frontend directory, and run main.py. The following command line options are available:

- `-v </path/to/file.txt>` - Allows the specification of a custom valid accounts file to use as input. Otherwise, the frontend will look in its directory for validAccounts.txt
- `-o </path/to/output>` - Allows the specification of a custom output directory for the transaction summary files. Otherwise, the frontend will create an `out` folder in its directory and place the transaction summary files there.

### Running the Back End

Change to the src/backend directory, and run main.py. The following command line options are REQUIRED:

- `-a </path/to/file.txt>` - Path to the input master accounts file from the previous day of transactions
- `-t </path/to/file.txt>` - Path to the merged transaction summary file from the previous day of transactions

The following command line options are OPTIONAL:

- `-v </path/to/file.txt>` - Allows the specification of a custom location for writing the new valid accounts file. Otherwise, the new valid accounts file will be written to `validaccounts.txt` in the script directory
- `-o </path/to/file.txt>` - Allows the specification of a custom loation for writing the new master accounts file. Otherwise, the new master accounts file will be written to `accountsfile.txt` in the script directory

### Running the integration script

Change to src/integration directory, and run `qbasicIntegration.sh`. No command line options are required.

It is recommended to redirect or tee the output from this script to a file for reading, as a massive amount of text will be written to standard output.

Post script cleanup/reset is handled by `refresh.sh`

### Running the automated testing

Change to test directory, and run `run_test.sh`. This script will run pytest with the required options and produce a report for viewing. The report will be opened in `less` by default after it is created.
