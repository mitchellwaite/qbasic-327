import messages
import session
import os


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


def doCreateAcct(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):

    if sessionType == session.loggedOutSessionType:
        print messages.getMessage("mustBeAgent","create an account")
        return False, None, None
    elif sessionType != session.privilegedSessionType:
        print messages.getMessage("mustBeAgent","create an account")
        return False, None, None
    else:
        accountNumber = raw_input(messages.getMessage("pleaseEnter","account number") + "> ")

        if len(accountNumber) != 7  or accountNumber.startswith(" ") or accountNumber.endswith(" ") or accountNumber.startswith("0"):
            pass



def doDeleteAcct():
    pass

def doWithdraw():
    pass

def doDeposit():
    pass

def doTransfer():
    pass
