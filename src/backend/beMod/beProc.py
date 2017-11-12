import messages
import beUtil

def loadMasterAccountsFile(filePath):
    masterAccountsArr = beUtil.loadFileToArray(filePath)
    masterAccountsDict = {}

    for i in range(0,len(masterAccountsArr));
        if len(masterAccountsArr[i]) > 47:
            print messages.getMessage("fatalErrorLineLength",i)
            raise Exception

        accountNumber, accountDetails = parseMasterAccountsFileLine(masterAccountsArr[i])

        masterAccountsDict[accountNumber] = accountDetails

    return masterAccountsDict

def loadTransactionSummaryFile(filePath):
    rawMtsfArr = beUtil.loadFileToArray(filePath)

    for i in range(0,len(rawMtsfArr)):


def parseMasterAccountsFileLine(line):
    accountNumber = ""
    accountBalance = ""
    accountName = ""

    # Split the line in to the three fields, based on one space being the separator
    lineArr = line.split(' ')

    # There are a minimum of 3 fields in the line
    if len(lineArr) < 3:
        print messages.getMessage("fatalErrorFieldCount",["master accounts file"],line])
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
    return accountNumber, { "name" : accountName, "balance" : accountBalance }

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
        print messages.getMessage("fatalErrorFieldCount",["transaction summary file",line])
        raise Exception

    code = lineArr[0]

    beUtil.validateTransactionCode(code, line)

    toAcct = lineArr[1]

    beUtil.validateAccountNumber(toAcct, line)

    amount = lineArr[2]

    beUtil.validateCentsAmount(amount, line)

    fromAcct = lineArr[3]

    beUtil.validateAccountNumber(fromAcct, line, code)

    name = " ".join(lineArr[4:])

    beUtil.validateAccountName(name, line, code)

    transaction = {
        "code" : code,
        "amount" : amount,
        "from" : fromAcct,
        "to" : toAcct,
        "name" : name
    }

    return transaction
