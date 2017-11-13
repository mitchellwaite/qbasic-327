import beMessages
import beUtil

def loadMasterAccountsFile(filePath):
    masterAccountsArr = beUtil.loadFileToArray(filePath)
    masterAccountsDict = {}

    for i in range(0,len(masterAccountsArr)):
        if len(masterAccountsArr[i]) > 47:
            print beMessages.getMessage("fatalErrorLineLength",i)
            raise Exception

        accountNumber, accountDetails = parseMasterAccountsFileLine(masterAccountsArr[i])

        if accountNumber not in masterAccountsDict:
            masterAccountsDict[accountNumber] = accountDetails
        else:
            print beMessages.getMessage("duplicateAccountMAF",accountNumber)
            raise Exception

    return masterAccountsDict

def loadTransactionSummaryFile(filePath):
    rawMtsfArr = beUtil.loadFileToArray(filePath)
    outMtsfArr = []

    for i in range(0,len(rawMtsfArr)):
        transaction = parseTransactionSummaryLine(rawMtsfArr[i])

        if transaction != None:
            outMtsfArr.append(transaction)
        else:
            if i < len(rawMtsfArr) - 1:
                # We've encountered a transaction file that has lines after the last one in the files
                print beMessages.getMessage("fatalError",["loadTSF","EOS isn't the last transaction in the file."])
                raise Exception

    return outMtsfArr

def parseMasterAccountsFileLine(line):
    accountNumber = ""
    accountBalance = ""
    accountName = ""

    # Split the line in to the three fields, based on one space being the separator
    lineArr = line.split(' ')

    # There are a minimum of 3 fields in the line
    if len(lineArr) < 3:
        print beMessages.getMessage("fatalErrorFieldCount",["master accounts file",line])
        raise Exception

    # Account number should be the first field
    accountNumber = lineArr[0]

    # Check the validity of the account number.
    beUtil.validateAccountNumber(accountNumber, line)

    # Account balance should be the second field
    accountBalance = lineArr[1]

    # Ensure it's an integer
    beUtil.validateCentsAmount(accountBalance, line)

    # Account name will be the rest of the fields
    accountName = " ".join(lineArr[2:])

    # check if it begins or ends with a space, is less than 3, or greater than  30
    beUtil.validateAccountName(accountName, line)

    # At this point, we have a valid account. Return a dict representation
    return accountNumber, { "name" : accountName, "balance" : int(accountBalance) }

def parseTransactionSummaryLine(line):
    code = ""
    amount = ""
    fromAcct = ""
    toAcct = ""
    name = ""

    # Split the line in to the three fields, based on one space being the separator
    lineArr = line.split(' ')

    # There are a minimum of 5 fields in the line
    if len(lineArr) < 5:
        print beMessages.getMessage("fatalErrorFieldCount",["transaction summary file",line])
        raise Exception

    code = lineArr[0]

    if code == "EOS":
        #End of session code. Indicate this by returning null so callers stop parsing the file!
        return None

    beUtil.validateTransactionCode(code)

    toAcct = lineArr[1]

    beUtil.validateAccountNumber(toAcct)

    amount = lineArr[2]

    beUtil.validateCentsAmount(amount, code)

    fromAcct = lineArr[3]

    beUtil.validateAccountNumber(fromAcct, code)

    name = " ".join(lineArr[4:])

    beUtil.validateAccountName(name, code)

    transaction = {
        "code" : code,
        "amount" : amount,
        "from" : fromAcct,
        "to" : toAcct,
        "name" : name,
        "str" : line
    }

    return transaction

def runTransaction(tx, accountsDict):
    if tx["code"] == "NEW":
        if tx["to"] in accounsDict.keys:
            # If the account exists, print an error
            print beMessages.getMessage("accountExistsErr",[tx["str"],tx["to"]])
        else:
            # If the account doesn't exist, create it
            accountsDict[tx["to"]] = {"name": tx["name"], "balance" : 0 }

    else:
        # For the rest of the transactions, the "to field must be specified"
        if tx["to"] not in accountsDict.keys():
            print beMessages.getMessage("accountDoesntExistErr",[tx["str"],tx["to"]])

        else:

            if tx["code"] ==  "DEL":
                if tx["name"] != accountsDict[tx["to"]]["name"]:
                    print beMessages.getMessage("accountNameMismatch",[tx["str"],tx["to"]])

                elif accountsDict[tx["to"]]["balance"] != 0:
                    print beMessages.getMessage("accountBalanceNotZero",[tx["str"],tx["to"]])

                else:
                    # Delete the account
                    del accountsDict[tx["to"]]

            elif tx["code"] == "WDR":
                if accountsDict[tx["to"]]["balance"] - int(tx["amount"]) < 0:
                    print beMessages.getMessage("accountBalanceLessThanZero",[tx["str"],tx["to"]])

                else:
                    accountsDict[tx["to"]] -= int(tx["amount"])

            elif tx["code"] == "DEP":
                if accountsDict[tx["to"]]["balance"] + int(tx["amount"]) > 99999999:
                    print beMessages.getMessage("accountBalanceMoreThanMax",[tx["str"],tx["to"]])

                else:
                    accountsDict[tx["to"]] += int(tx["amount"])

            elif tx["code"] == "XFR":
                # Oh boy, special cases!
                if tx["from"] not in accounsDict.keys:
                    print beMessages.getMessage("accountDoesntExistErr",[tx["str"],tx["from"]])

                elif accountsDict[tx["from"]]["balance"] - int(tx["amount"]) < 0:
                    print beMessages.getMessage("accountBalanceLessThanZero",[tx["str"],tx["from"]])

                elif accountsDict[tx["to"]]["balance"] + int(tx["amount"]) > 99999999:
                    print beMessages.getMessage("accountBalanceMoreThanMax",[tx["str"],tx["to"]])

                else:
                    accountsDict[tx["from"]] -= int(tx["amount"])
                    accountsDict[tx["to"]] += int(tx["amount"])

    return accountsDict

def writeMasterAccountsFile(outFile, accountsDict):
    for account in sorted(accountsDict.keys()):
        outString = "{} {} {}\n".format(account,
                                        beUtil.zeroPad(str(accountsDict[account]["balance"])),
                                        accountsDict[account]["name"])
        outFile.write(outString)

def writeValidAccountsList(outFile, accountsDict):
    for account in sorted(accountsDict.keys()):
        outFile.write(account + "\n")
