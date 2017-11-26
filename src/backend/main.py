#!/usr/bin/env python
# FILE: main.py
# DESC: Main python script of the QBasic backend
from beMod import *
import os
import sys
import getopt

def main():

    # Variables to keep track of the locations of the input/output files
    masterAccountsFilePath = ""
    mergedTransactionSummaryFilePath = ""
    outputValidAccountsFilePath = "validaccounts.txt"
    outputMasterAccountsFilePath = "accountsfile.txt"

    # Variables to keep track of actual data
    transactionList = []
    accountsDict = {}

    # File handles
    outValidAccountsFile = None
    outMasterAccountsFile = None

    #Print a test message
    print beMessages.getMessage("test")

    try:
        # Get the command line options
        opts, args = getopt.getopt(sys.argv[1:], "a:t:v:o:")

        for opt, arg in opts:
            if opt == "-a":
                # Path to the valid accounts file
                masterAccountsFilePath = arg
                print beMessages.getMessage("masterAccountsLoc", arg)
            elif opt == "-t":
                # Path to the place we want to store the transaction lists
                mergedTransactionSummaryFilePath = arg
                print beMessages.getMessage("mergedSummLoc", arg)
            elif opt == "-v":
                outputValidAccountsFilePath = arg
                print beMessages.getMessage("outValidAccLoc", arg)
            elif opt == "-o":
                outputMasterAccountsFilePath = arg
                print beMessages.getMessage("outMasterAccLoc", arg)

    except Exception as e:
        print beMessages.getMessage("fatalError", str(e))
        return -1

    # Check to make sure the old master accounts file actually exists. If not,
    # print an error and return
    if not os.path.exists(masterAccountsFilePath):
        print beMessages.getMessage("fatalError",["main","Old master accounts file not found"])
        return -1

    # Check to make sure the merged transaction summary file actually exists.
    # If not, print an error and return
    if not os.path.exists(mergedTransactionSummaryFilePath):
        print beMessages.getMessage("fatalError",["main","Merged transaction summary file not found"])
        return -1

    # Open the new valid accounts list and master accounts file for writing.
    # If there's a problem, an exception will be thrown and the backend will die.
    outMasterAccountsFile = open(outputMasterAccountsFilePath,'w')
    outValidAccountsFile = open(outputValidAccountsFilePath, 'w')

    # Parse and load the old master accounts file
    accountsDict = beProc.loadMasterAccountsFile(masterAccountsFilePath)

    # Parse and load the merged transaction summary file
    transactionList = beProc.loadTransactionSummaryFile(mergedTransactionSummaryFilePath)

    # In order, run each transaction against the accounts dictionary, updating
    # it if the transaction was successful. We're assuming that the previous
    # loading functions have checked for well formed data
    for tx in transactionList:
        accountsDict = beProc.runTransaction(tx, accountsDict)

    # Write the valid accounts list
    beProc.writeValidAccountsList(outValidAccountsFile, accountsDict)

    # Write the new master accounts file
    beProc.writeMasterAccountsFile(outMasterAccountsFile, accountsDict)

    # Close both files
    outValidAccountsFile.close()
    outMasterAccountsFile.close()

    # Print a finished message.
    print "QBasic backend processing finished.\n"

if __name__ == "__main__":
    main()
