#!/usr/bin/env python
# FILE: main.py
# DESC: Main python script of the QBasic backend
from beMod import *
import sys
import getopt

def main():

    # Variables to keep track of the locations of the input/output files
    masterAccountsFile = ""
    mergedTransactionSummaryFile = ""
    outputValidAccountsFile = "validaccounts.txt"
    outputMasterAccountsFile = "accountsfile.txt"

    #Print a test message
    print messages.getMessage("test")

    try:
        # Get the command line options
        opts, args = getopt.getopt(sys.argv[1:], "a:t:v:o:")

        for opt, arg in opts:
            if opt == "-a":
                # Path to the valid accounts file
                masterAccountsFile = arg
                print messages.getMessage("masterAccountsLoc", arg)
            elif opt == "-t":
                # Path to the place we want to store the transaction lists
                transactionListPath = arg
                print messages.getMessage("mergedSummLoc", arg)
    except Exception as e:
        print messages.getMessage("fatalError", str(e))
        return -1

if __name__ == "__main__":
    main()
