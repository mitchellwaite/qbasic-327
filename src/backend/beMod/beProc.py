# FILE: beProc.py
# DESC: Data processing/file parsing functions for QBasic backend
import beMessages
import beUtil

# Loads the master accounts file from the disk, parsing each line to Ensure
# well-formed data.
#
# @param filePath -> string -> path to the master accounts file
# @return dict -> dictionary representation of the master accounts file
def loadMasterAccountsFile(filePath):
    # Load the file specified by filePath to an array of lines
    masterAccountsArr = beUtil.loadFileToArray(filePath)
    # Initialize a blank dictionary
    masterAccountsDict = {}

    # For each line in the array
    for i in range(0,len(masterAccountsArr)):
        # Check to make sure its at maximum 47 characters. If not, print message
        # and throw an error.
        if len(masterAccountsArr[i]) > 47:
            print beMessages.getMessage("fatalErrorLineLength",i)
            raise Exception

        # Call the line parsing function. If there's any problems, an exception
        # will be thrown
        accountNumber, accountDetails = parseMasterAccountsFileLine(masterAccountsArr[i])

        # If the account does not already exist in the dictionary
        if accountNumber not in masterAccountsDict:
            # Add it to the accounts dictionary, using the account number as the key
            masterAccountsDict[accountNumber] = accountDetails
        else:
            # If the account exists already, there is a problem with the MAF
            # Print a messsage and throw an exception
            print beMessages.getMessage("duplicateAccountMAF",accountNumber)
            raise Exception

    # return the master accounts dictionary
    return masterAccountsDict

# Loads the merged tx summary file from the disk, parsing each line to Ensure
# well-formed data.
#
# @param filePath -> string -> path to the transaction summary File
# @return array -> array representation of the master accounts file
def loadTransactionSummaryFile(filePath):
    # Load the file specified by filePath to an array of lines
    rawMtsfArr = beUtil.loadFileToArray(filePath)
    # Initialize a blank output array. We want to keep these transactions in
    # the same order as the MTSF
    outMtsfArr = []

    # Process the input array in order
    for i in range(0,len(rawMtsfArr)):
        # Parse a line of the transaction file
        transaction = parseTransactionSummaryLine(rawMtsfArr[i])

        # The parsing function returns None to signal an EOS transaction. Don't
        # append this to the transaction file
        if transaction != None:
            outMtsfArr.append(transaction)
        else:
            # If an EOS is not the last transaction in the fil
            if i < len(rawMtsfArr) - 1:
                # print an error and throw an exception
                print beMessages.getMessage("fatalError",["loadTSF","EOS isn't the last transaction in the file."])
                raise Exception

    return outMtsfArr

# Parses a line of the master accounts file.
#
# @param line -> string -> line to parse
# @return string -> account number of the parsed line
# @return dict -> dict containing the name and balance of the account
def parseMasterAccountsFileLine(line):
    # Variables to keep track of the account information
    accountNumber = ""
    accountBalance = ""
    accountName = ""

    # Split the line in to the three fields, based on one space being the separator
    lineArr = line.split(' ')

    # There are a minimum of 3 fields in the line. If there are less
    # we have a problem
    if len(lineArr) < 3:
        print beMessages.getMessage("fatalErrorFieldCount",["master accounts file",line])
        raise Exception

    # Account number should be the first field
    accountNumber = lineArr[0]

    # Check the validity of the account number.
    beUtil.validateAccountNumber(accountNumber, line)

    # Account balance should be the second field
    accountBalance = lineArr[1]

    # Ensure it's a valid monetary amount
    beUtil.validateCentsAmount(accountBalance, line)

    # Account name will be the rest of the fields
    accountName = " ".join(lineArr[2:])

    # check if it begins or ends with a space, is less than 3, or greater than  30
    beUtil.validateAccountName(accountName, line)

    # At this point, we have a valid account. Return a dict representation
    return accountNumber, { "name" : accountName, "balance" : int(accountBalance) }

# Parses a line of the master accounts file.
#
# @param line -> string -> line to parse
# @return dict -> dict containing a representation of the transaction, or None if transaction is EOS
def parseTransactionSummaryLine(line):
    code = ""
    amount = ""
    fromAcct = ""
    toAcct = ""
    name = ""

    # Split the line in to different fields, based on one space being the separator
    lineArr = line.split(' ')

    # There are a minimum of 5 fields in the line.
    if len(lineArr) < 5:
        print beMessages.getMessage("fatalErrorFieldCount",["transaction summary file",line])
        raise Exception

    #Transaction code should be the first field
    code = lineArr[0]


    if code == "EOS":
        #End of session code. Indicate this by returning null so callers stop parsing the file!
        return None
    else:
        # Validate the transaction code is on the allowed list
        beUtil.validateTransactionCode(code)

    # The "to" account number should be the second field
    toAcct = lineArr[1]

    # Ensure the account number is valid
    beUtil.validateAccountNumber(toAcct)

    # Transaction amount should be the third field
    amount = lineArr[2]

    # Ensure it's a valid monetary amount
    beUtil.validateCentsAmount(amount, code)

    # The "from" account number shoudl be the fourth field
    fromAcct = lineArr[3]

    # Ensure the from account is valid for the specified transaction code.
    # For single account transactions, this field is unused. For XFR, this
    # should be a regular account number
    beUtil.validateFromAccountNumber(fromAcct, code)

    # Account name will be the rest of the fields
    name = " ".join(lineArr[4:])

    # Ensure the account name is valid for the specified transaction code.
    # For NEW and DEL, this is a regular account name. For all others, it is
    # an unused field.
    beUtil.validateAccountName(name, code)

    # Construct a dict representation of the transaction
    transaction = {
        "code" : code,
        "amount" : amount,
        "from" : fromAcct,
        "to" : toAcct,
        "name" : name,
        "str" : line
    }

    # Return the transaction
    return transaction

# Ensures that a transaction adding money to an account won't make the balance
# exceed an 8 digit amount
#
# @param accountsDict -> dict -> dictionary of accounts
# @param tx -> dict -> the transaction to check
# @param accountKey -> string -> controls which account in the transaction we check
# @return -> bool -> True if the account balance violates constraints, false otherwise
def exceedsMaxBalance(accountsDict, tx, accountKey):
    if accountsDict[tx[accountKey]]["balance"] + int(tx["amount"]) > 99999999:
        return True
    else:
        return False

# Ensures that a transaction removing money from an account won't make the balance
# less than zero
#
# @param accountsDict -> dict -> dictionary of accounts
# @param tx -> dict -> the transaction to check
# @param accountKey -> string -> controls which account in the transaction we check
# @return -> bool -> True if the account balance violates constraints, false otherwise
def subceedsMinBalance(accountsDict, tx, accountKey):
    if accountsDict[tx[accountKey]]["balance"] - int(tx["amount"]) < 0:
        return True
    else:
        return False

# Checks transactions against the master accounts dictionary to ensure they
# meet constraints. If they do, process the transaction and update the master
# accounts dictionary
#
# @param tx -> dict -> the transaction to proces
# @param accountsDict -> dict -> the accounts dictionary to process the transaction against.
#
# @return dict -> the original accounts dict if the transaction does not meet constraints
#                 otherwise, the updated accounts dict if the transaction was valid.
def runTransaction(tx, accountsDict):
    # NEW account transaction
    if tx["code"] == "NEW":
        # !SPECIAL CASE! New account is the only one that throws an error
        # if the account already exists
        if tx["to"] in accountsDict.keys():
            # If the account exists, print an error
            print beMessages.getMessage("accountExistsErr",[tx["str"],tx["to"]])
        else:
            # If the account doesn't exist, create it
            accountsDict[tx["to"]] = {"name": tx["name"], "balance" : 0 }

    else:
        # For the rest of the transactions, the "to" account must be specified
        # and present in the master accounts file
        if tx["to"] not in accountsDict.keys():
            print beMessages.getMessage("accountDoesntExistErr",[tx["str"],tx["to"]])

        else:

            # DELETE account transaction
            if tx["code"] ==  "DEL":
                # Ensure the name matches before deletion
                if tx["name"] != accountsDict[tx["to"]]["name"]:
                    print beMessages.getMessage("accountNameMismatch",[tx["str"],tx["to"]])

                # Ensure that the account balance is zero before deletion
                elif accountsDict[tx["to"]]["balance"] != 0:
                    print beMessages.getMessage("accountBalanceNotZero",[tx["str"],tx["to"]])

                else:
                    # Delete the account
                    del accountsDict[tx["to"]]

            elif tx["code"] == "WDR":
                # Ensure you can't withdraw more money than what the account contains
                if subceedsMinBalance(accountsDict, tx, "to"):
                    print beMessages.getMessage("accountBalanceLessThanZero",[tx["str"],tx["to"]])

                else:
                    # Subtract the amount of money withdrawn from the account
                    accountsDict[tx["to"]]["balance"] -= int(tx["amount"])


            elif tx["code"] == "DEP":
                # Ensure that the deposit won't make the account have more than an
                # 8 digit amount of money in it
                if exceedsMaxBalance(accountsDict, tx, "to"):
                    print beMessages.getMessage("accountBalanceMoreThanMax",[tx["str"],tx["to"]])

                else:
                    # Add the amount of money depsited to the account balance
                    accountsDict[tx["to"]]["balance"] += int(tx["amount"])

            elif tx["code"] == "XFR":
                # Oh boy, special cases!

                # For transfer, check that the from account exists
                if tx["from"] not in accounsDict.keys:
                    print beMessages.getMessage("accountDoesntExistErr",[tx["str"],tx["from"]])

                # Ensure the from account has enough money to complete the transfer
                elif subceedsMinBalance(accountsDict,tx,"from"):
                    print beMessages.getMessage("accountBalanceLessThanZero",[tx["str"],tx["from"]])

                # Ensure that the deposit won't make the "to" account have more than an
                # 8 digit amount of money in it
                elif exceedsMaxBalance(accountsDict, tx, "to") > 99999999:
                    print beMessages.getMessage("accountBalanceMoreThanMax",[tx["str"],tx["to"]])

                else:
                    # If the transfer is kosher, subtract the amount from
                    # the "from" account and add it to the "to" account
                    accountsDict[tx["from"]]["balance"] -= int(tx["amount"])
                    accountsDict[tx["to"]]["balance"] += int(tx["amount"])

    return accountsDict

# Writes the new master accounts file to disk. Loops through each key in sorted
# order
#
# @param outFile -> File -> file handle open for writing to
# @param accountsDict -> dict -> dict of accounts to get keys from
def writeMasterAccountsFile(outFile, accountsDict):
    # For each account in the sorted array of accounts
    for account in sorted(accountsDict.keys()):
        # Write the account, formatted with a newline and a zero padded balance
        outString = "{} {} {}\n".format(account,
                                        beUtil.zeroPad(str(accountsDict[account]["balance"])),
                                        accountsDict[account]["name"])
        outFile.write(outString)

# Writes the valid accounts file, essentially a sorted array of the keys of the
# accounts dictionary
#
# @param outFile -> File -> file handle open for writing to
# @param accountsDict -> dict -> dict of accounts to get keys from
def writeValidAccountsList(outFile, accountsDict):
    # For each key in a sorted array
    for account in sorted(accountsDict.keys()):
        # Write it to the file, appending a newline
        outFile.write(account + "\n")
