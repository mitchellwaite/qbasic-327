# FILE: tx.py
# DESC: Contains transaction related functions for QBasic
import messages
import session
import os
import qbUtil

# All makeTx(...) functions are wrappers for the main makeTx function
# They properly set up the transacton codes and values
# The names and parameters are named accordingly
# Return values are the return from makeTx
# All parameters are strings
def makeTxCreate(number,name):
    return makeTx("NEW",None,None,number,name)

def makeTxDelete(number,name):
    return makeTx("DEL",None,None,number,name)

def makeTxWithdraw(number, amt):
    return makeTx("WDR",amt,None,number,None)

def makeTxDeposit(number, amt):
    return makeTx("DEP",amt,None,number,None)

def makeTxTransfer(numberFrom, numberTo, amt):
    return makeTx("XFR",amt,numberFrom,numberTo,None)

# Mates a transaction object from the parameters passed in
#
# @param code -> string -> Transaction code
# @param amt -> int -> transaction monetary amount
# @param fromAcct -> int -> account to represent the "from" field
# @param toAcct -> int -> account to represent the "to" field
# @param name -> string -> account name
#
# @return dictionary -> dictionary containing a representation of the transaction
def makeTx(code, amt, fromAcct, toAcct, name):
    intAmt = "000"
    intFrom = "0000000"
    intName = "***"

    # The to account is optional. If it's provided, set the field
    if fromAcct is not None:
        intFrom = str(fromAcct)

    # Name is optional, if provided set the field
    if name is not None:
        intName = name

    # Transaction amount is optional. If provided, set the field
    if amt is not None:
        intAmt = str(amt)

    # Construct the transaction object
    transaction = {
        "code" : code,
        "amount" : intAmt,
        "from" : intFrom,
        "to" : toAcct,
        "name" : intName
    }

    # Return the constructed object
    return transaction

# Mates a final EOS transaction object
#
# @return dictionary -> dictionary containing a representation of
#                       a final EOS transaction
def makeFinalTx():
    transaction = {
        "code" : "EOS",
        "amount" : "000",
        "from" : "0000000",
        "to" : "0000000",
        "name" : "***"
    }

    return transaction

# Writes a provided transaction list to the specified directory
#
# @param txList -> list of dicts -> List of transaction objects
# @param txSummaryOutputDir -> string -> path to the transaction summary output directory
def writeTransactionList(txList, txSummaryOutputDir):
    fileCounter = 0
    outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    # We don't want to overwrite any transaction file, so loop to find one that
    # doesn't exist
    while os.path.exists(outputFilePath):
        # If the file exists, we want to make a new one
        fileCounter += 1
        outputFilePath = txSummaryOutputDir + "/txSummary_{}.txt".format(fileCounter)

    # Open the file for writing
    outFile = open(outputFilePath, 'w')

    # Append the final EOS transaction
    txList.append(makeFinalTx())

    # Write out the transaction list, line by line
    for tx in txList:
        outFile.write("{} {} {} {} {}\n".format(tx["code"], tx["to"], tx["amount"], tx["from"], tx["name"]))

    #Close the file
    outFile.close()

# Validates whether an account was new or deleted within the session
#
# @param action -> string -> name of transaction, used to format error messages
# @param accoutnNumber -> string -> accoutn number to validateNewDeleted
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
#
# @return boolean -> true if the account was not new or deleted, false otherwise
def validateNewDeleted(action, accountNumber, accountsPendingCreation, accountsPendingDeletion):
    # Check for existence of accountNumber in both lists. If they exist,
    # return false.
    if accountNumber in accountsPendingDeletion:
        print messages.getMessage("pendingDeletion",[action,accountNumber])
        return False
    elif accountNumber in accountsPendingCreation:
        print messages.getMessage("pendingCreation",[action,accountNumber])
        return False
    else:
        return True

# Function to get a valid account number from the user
#
# @param s -> string -> appends string to the prompt
#
# @return boolean -> whether the attempt to get the account number was successful
# @return string -> The account number
def getAcctNumber(s = ""):
    # Promt for the account number
    print messages.getMessage("pleaseEnter","account number" + s)
    accountNumber = raw_input("> ")

    # Check it meets the requirements. If it doesn't, print an error and bail out
    if len(accountNumber) != 7  or accountNumber.startswith(" ") or accountNumber.endswith(" ") or accountNumber.startswith("0") or not qbUtil.isInt(accountNumber):
        print messages.getMessage("invalidCustom",["account number", accountNumber])
        return False, None

    return True, accountNumber

# Function to get a valid account number and name from the user
#
#
# @return boolean -> whether the attempt to get the account info was successful
# @return string -> the account name
# @return string -> The account number
def getAcctNameNumber():
    # Call the accountNumber function above
    result, accountNumber = getAcctNumber()

    # If it failed, bail out
    if False == result:
        return False, None, None

    # Get the account name
    print messages.getMessage("pleaseEnter","account name")
    accountName = raw_input("> ")

    # Check it meets the requirements. If it doesn't, print an error and bail out
    if len(accountName) < 3 or len(accountName) > 30 or accountName.startswith(" ") or accountName.endswith(" "):
        print messages.getMessage("invalidCustom",["account name",accountName])
        return False, None, None

    # The accoutn name and number are good. Return them
    return True, accountName, accountNumber

# Function to get a dollar amount from the user.
#
# @param sessionType -> sring -> represents the session type, used for the different
#                                transaction limits in machine/agent mode
#
# @return boolean -> whether the attempt to get the amount was successful
# @return int -> amount of cents
def getDollarAmount(sessionType):

    # Prompt for an amount of cents from the user
    print messages.getMessage("pleaseEnter","an amount of money in cents")
    centsAmount = raw_input("> ")

    # Check to make sure it's an int. If not, print an error bail out of the function
    if not qbUtil.isInt(centsAmount):
        print messages.getMessage("invalidCustom",["monetary amount", qbUtil.centsToDollars(centsAmount)])
        return False, None

    # Convert the amount to an integer
    centsAmountInt = int(centsAmount)

    # Check the amount to make sure its within the limit for the specified session
    # type. If it isn't print an error and bail out of the function
    if sessionType != session.privilegedSessionType and centsAmountInt > 100000:
        print messages.getMessage("mustBeAgent","execute transactions over $1000")
        return False, None
    elif centsAmountInt <= 0 or centsAmountInt > 99999999:
        print messages.getMessage("invalidCustom",["monetary amount", qbUtil.centsToDollars(centsAmount)])
        return False, None

    # Return the amount of cents
    return True, centsAmountInt

# Perform the checks and does the create account transaction
#
# @param sessionType -> string -> current session type
# @param validAccounts -> list -> list of valid accounts
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
#
# @return boolean -> whether the create account succeeded
# @return dict -> the transaction object, passed up from makeTx
# @return string -> the account number for the transaction
def doCreateAcct(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):
    # Check if the session type is not logged in, or is not agent
    # If that's the case, bail out of the function
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

        # If the account number is in the valid list, we can't create it
        # Bail out of the function
        if accountNumber in validAccounts:
            print messages.getMessage("accountAlreadyExists",accountNumber)
            return False, None, None

        # I think we're good to make the transaction at this point
        transaction = makeTxCreate(accountNumber, accountName)

        return True, transaction, accountNumber

# Perform the checks and does the delete account transaction
#
# @param sessionType -> string -> current session type
# @param validAccounts -> list -> list of valid accounts
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
#
# @return boolean -> whether the delete account succeeded
# @return dict -> the transaction object, passed up from makeTx
# @return string -> the account number for the transaction
def doDeleteAcct(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):
        # Check if the session type is not logged in, or is not agent
        # If that's the case, bail out of the function
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

            # Make the delete transaction
            transaction = makeTxDelete(accountNumber, accountName)

            return True, transaction, accountNumber

# Perform the checks and does the deposit transaction
#
# @param sessionType -> string -> current session type
# @param validAccounts -> list -> list of valid accountsPendingCreation
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
#
# @return boolean -> whether the deposit succeeded
# @return dict -> the transaction object, passed up from makeTx
# @return string -> the account number for the transaction
# @return int -> the dollar amount of the transaction
def doDeposit(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):
    # Check if the session type is not logged in
    # If that's the case, bail out of the function
    if sessionType == session.loggedOutSessionType:
        print messages.getMessage("txErrNotLoggedIn")
        return False, None, None, None
    else:
        # Get the acct name and number
        result, accountNumber = getAcctNumber()

        if False == result:
            # There was an error getting the account info from the user
            return False, None, None, None

        # Validate that the account isn't a new or deleted account
        if False == validateNewDeleted("deposit",accountNumber,accountsPendingCreation, accountsPendingDeletion):
            return False, None, None, None

        # Check if the account actually exists
        if accountNumber not in validAccounts:
            print messages.getMessage("accountDoesntExist",accountNumber)
            return False, None, None, None

        # Get the dollar amount from the user
        result, dollarAmount = getDollarAmount(sessionType)

        if False == result:
            # There was an error getting the dollar amount from the user
            return False, None, None, None

        # Make the deposit transaction
        transaction = makeTxDeposit(accountNumber, dollarAmount)

        return True, transaction, accountNumber, dollarAmount

# Perform the checks and does the transfer transaction
#
# @param sessionType -> string -> current session type
# @param validAccounts -> list -> list of valid accountsPendingCreation
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
#
# @return boolean -> whether the deposit succeeded
# @return dict -> the transaction object, passed up from makeTx
# @return string -> the account number we are transferring to
# @return int -> the dollar amount of the transaction
def doTransfer(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion):
    # Check if the session type is not logged in
    # If that's the case, bail out of the function
    if sessionType == session.loggedOutSessionType:
        print messages.getMessage("txErrNotLoggedIn")
        return False, None, None, None
    else:
        # Get the acct name and number
        result, accountNumberFrom = getAcctNumber(" to transfer from")

        # Validate that the account isn't a new or deleted account
        if False == validateNewDeleted("transfer",accountNumberFrom,accountsPendingCreation, accountsPendingDeletion):
            return False, None, None, None

        # Check if the account actually exists
        if accountNumberFrom not in validAccounts:
            print messages.getMessage("accountDoesntExist",accountNumberFrom)
            return False, None, None, None

        # Get the acct name and number
        result, accountNumberTo = getAcctNumber(" to transfer to")

        # Validate that the account isn't a new or deleted account
        if False == validateNewDeleted("transfer",accountNumberTo,accountsPendingCreation, accountsPendingDeletion):
            return False, None, None, None

        # Check if the account actually exists
        if accountNumberTo not in validAccounts:
            print messages.getMessage("accountDoesntExist",accountNumberTo)
            return False, None, None, None

        # Check if "from" and "to" accounts are the same
        if accountNumberFrom == accountNumberTo:
            print messages.getMessage("transferSameAccountError")
            return False, None, None, None

        # Get the dollar amount from the user
        result, dollarAmount = getDollarAmount(sessionType)

        if False == result:
            # There was an error getting the dollar amount from the user
            return False, None, None, None

        # Make the transfer transaction
        transaction = makeTxTransfer(accountNumberFrom, accountNumberTo, dollarAmount)

        return True, transaction, accountNumberTo, dollarAmount

# Perform the checks and does the deposit transaction
#
# @param sessionType -> string -> current session type
# @param validAccounts -> list -> list of valid accountsPendingCreation
# @param accountsPendingCreation -> list -> list of accoutnts pending creation
# @param accountsPendingDeletion -> list -> list of accounts pending deletion
# @param accountsWithdrawalDict -> dict -> list of accounts and the amount
#                                          withdrawn in the current session
#
# @return boolean -> whether the deposit succeeded
# @return dict -> the transaction object, passed up from makeTx
# @return string -> the account number for the transaction
# @return int -> the dollar amount of the transaction
def doWithdraw(sessionType, validAccounts, accountsPendingCreation, accountsPendingDeletion, accountsWithdrawalDict):
        # Check if the session type is not logged in
        # If that's the case, bail out of the function
        if sessionType == session.loggedOutSessionType:
            print messages.getMessage("txErrNotLoggedIn")
            return False, None, None, None
        else:
            # Get the acct name and number
            result, accountNumber = getAcctNumber()

            if False == result:
                # There was an error getting the account info from the user
                return False, None, None, None

            # Validate that the account isn't a new or deleted account
            if False == validateNewDeleted("withdraw",accountNumber,accountsPendingCreation, accountsPendingDeletion):
                return False, None, None, None

            # Check if the account actually exists
            if accountNumber not in validAccounts:
                print messages.getMessage("accountDoesntExist",accountNumber)
                return False, None, None, None

            result, dollarAmount = getDollarAmount(sessionType)

            if False == result:
                # There was an error getting the dollar amount from the user
                return False, None, None, None

            #check to see if we would hit a withdrawal limit
            if sessionType != session.privilegedSessionType:
                if accountNumber in accountsWithdrawalDict:
                    if (accountsWithdrawalDict[accountNumber] + int(dollarAmount)) > 100000:
                        #We can't go over $1000 in a session
                        print messages.getMessage("withdrawLimitErr",accountNumber)
                        return False, None, None, None

            # Make the withdrawal transaction
            transaction = makeTxWithdraw(accountNumber, dollarAmount)

            return True, transaction, accountNumber, dollarAmount
