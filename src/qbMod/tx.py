import messages, session, os

class Factory:
    @staticmethod
    def makeTxCreate(number,name):
        return makeTx("NEW",number,None,None,name)

    @staticmethod
    def makeTxDelete(number,name):
        return makeTx("DEL",number,None,None,name)

    @staticmethod
    def makeTxWithdraw(number, amt):
        return makeTx("WDR",number,None,None,name)

    @staticmethod
    def makeTxDeposit():
        return makeTx("DEP",number,None,None,name)

    @staticmethod
    def makeTxTransfer():
        return makeTx("XFR",number,None,None,name)

    @staticmethod
    def makeTx(code, amt, fromAcct, toAcct, name):
        intAmt = "000"
        intTo = "0000000"
        intName = "***"

        if toAcct is not None:
            intTo = str(to)

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

    @staticmethod
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
    outputList = []
    outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    while os.path.exists(outputFilePath):
        # If the file exists, we want to make a new one
        fileCounter += 1
        outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    outFile = open(outputFilePath, 'w')

    txList.append(Factory.makeFinalTx())
    for tx in txList:
        outFile.write("{} {} {} {} {}\n".format(tx["code"], tx["amount"], tx["from"], tx["to"], tx["name"]))

    outFile.close()


def doCreateAcct():
    pass

def doDeleteAcct():
    pass

def doWithdraw():
    pass

def doDeposit():
    pass

def doTransfer():
    pass
