import messages
import session
import os
import qbUtil

def makeTxCreate(number,name):
    return makeTx("NEW",None,number,None,name)

def makeTxDelete(number,name):
    return makeTx("DEL",None,number,None,name)

def makeTxWithdraw(number, amt):
    return makeTx("WDR",amt,number,None,None)

def makeTxDeposit(number, amt):
    return makeTx("DEP",amt,number,None,None)

def makeTxTransfer(numberFrom, numberTo, amt):
    return makeTx("XFR",amt,numberFrom,numberTo,None)

def makeTx(code, amt, fromAcct, toAcct, name):
    intAmt = "000"
    intTo = "0000000"
    intName = "***"

    if toAcct is not None:
        intTo = str(toAcct)

    if name is not None:
        intName = name

    if amt is not None:
        intAmt = str(amt)

    transaction = {
        "code" : code,
        "amount" : intAmt,
        "from" : fromAcct,
        "to" : intTo,
        "name" : intName
    }

    return transaction

def makeFinalTx():
    transaction = {
        "code" : "EOS",
        "amount" : "000",
        "from" : "0000000",
        "to" : "0000000",
        "name" : "***"
    }

    return transaction

def writeTransactionList(txList, txSummaryOutputDir):
    fileCounter = 0
    outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    while os.path.exists(outputFilePath):
        # If the file exists, we want to make a new one
        fileCounter += 1
        outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    outFile = open(outputFilePath, 'w')

    txList.append(makeFinalTx())
    for tx in txList:
        outFile.write("{} {} {} {} {}\n".format(tx["code"], tx["amount"], tx["from"], tx["to"], tx["name"]))

    outFile.close()

def validateNewDeleted(action, accountNumber, accountsPendingCreation, accountsPendingDeletion):
    if accountNumber in accountsPendingDeletion:
        print messages.getMessage("pendingDeletion",[action,accountNumber])
        return False
    elif accountNumber in accountsPendingCreation:
        print messages.getMessage("pendingCreation",[action,accountNumber])
        return False
    else:
        return True

def getAcctNameNumber():
    accountNumber = raw_input(messages.getMessage("pleaseEnter","account number") + "> ")

    if len(accountNumber) != 7  or accountNumber.startswith(" ") or accountNumber.endswith(" ") or accountNumber.startswith("0") or not qbUtil.isInt(accountNumber):
        print messages.getMessage("invalidCustom",["account number", accountNumber])
        return False, None, None

    accountName = raw_input(messages.getMessage("pleaseEnter","account name") + "> ")

    if len(accountName) < 3 or len(accountName) > 30 or accountName.startswith(" ") or accountName.endswith(" "):
        print messages.getMessage("invalidCustom",["account name",accountName])
        return False, None, None

    return True, accountName, accountNumber

def doCreateAcct(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):

    if sessionType == session.loggedOutSessionType:
        print messages.getMessage("txErrNotLoggedIn")
        return False, None, None
    elif sessionType != session.privilegedSessionType:
        print messages.getMessage("mustBeAgent","create an account")
        return False, None, None
    else:

        # Get the acct name and number
        result, accountName, accountNumber = getAcctNameNumber()

        if False == result:
            # There was an error getting the account info from the user
            return False, None, None

        # Validate that the account isn't a new or deleted account
        if False == validateNewDeleted("create account",accountNumber,accountsPendingCreation, accountsPendingDeletion):
            return False, None, None

        if accountNumber in validAccounts:
            print messages.getMessage("accountAlreadyExists",accountNumber)
            return False, None, None

        # I think we're good to make the transaction at this point
        transaction = makeTxCreate(accountNumber, accountName)

        return True, transaction, accountNumber

def doDeleteAcct(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):
        if sessionType == session.loggedOutSessionType:
            print messages.getMessage("txErrNotLoggedIn")
            return False, None, None
        elif sessionType != session.privilegedSessionType:
            print messages.getMessage("mustBeAgent","delete an account")
            return False, None, None
        else:
            # Get the acct name and number
            result, accountName, accountNumber = getAcctNameNumber()

            if False == result:
                # There was an error getting the account info from the user
                return False, None, None

            # Validate that the account isn't a new or deleted account
            if False == validateNewDeleted("delete account",accountNumber,accountsPendingCreation, accountsPendingDeletion):
                return False, None, None

            # Check if the account actually exists
            if accountNumber not in validAccounts:
                print messages.getMessage("accountDoesntExist",accountNumber)
                return False, None, None

            transaction = makeTxDelete(accountNumber, accountName)

            return True, transaction, accountNumber

def doWithdraw():
    pass

def doDeposit():
    pass

def doTransfer():
    pass
