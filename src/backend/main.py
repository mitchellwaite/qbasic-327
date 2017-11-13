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
                outputValidAccountsFilePath = args
                print beMessages.getMessage("outValidAccLoc", arg)
            elif opt == "-o":
                outputMasterAccountsFilePath = args
                print beMessages.getMessage("outMasterAccLoc", arg)

    except Exception as e:
        print beMessages.getMessage("fatalError", str(e))
        return -1

    if not os.path.exists(masterAccountsFilePath):
        print beMessages.getMessage("fatalError",["main","Old master accounts file not found"])
        return -1

    if not os.path.exists(mergedTransactionSummaryFilePath):
        print beMessages.getMessage("fatalError",["main","Merged transaction summary file not found"])
        return -1

    #Open the new valid accounts list and master accounts file for writing
    outMasterAccountsFile = open(outputMasterAccountsFilePath,'w')
    outValidAccountsFile = open(outputValidAccountsFilePath, 'w')

    # Parse and load the old master accounts file
    accountsDict = beProc.loadMasterAccountsFile(masterAccountsFilePath)

    # Parse and load the merged transaction summary file
    transactionList = beProc.loadTransactionSummaryFile(mergedTransactionSummaryFilePath)

    # In order, run each transaction against the accounts dictionary, updating
    # it if the transaction was successful. We're assuming that the previous
    # code has checked for well formed data at this point
    for tx in transactionList:
        accountsDict = beProc.runTransaction(tx, accountsDict)

    # Write the valid accounts list
    beProc.writeValidAccountsList(outValidAccountsFile, accountsDict)

    # Write the new master accounts file
    beProc.writeMasterAccountsFile(outMasterAccountsFile, accountsDict)

    outValidAccountsFile.close()
    outMasterAccountsFile.close()

if __name__ == "__main__":
    main()
