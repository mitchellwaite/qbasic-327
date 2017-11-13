# FILE: beUtil.py
# DESC: Utility functions for QBasic backend components

import beMessages

# Returns true if the string passed in represents an intger, false otherwise
#
# @param s -> string -> to test if it can be converted to an integer
# @return -> boolean
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Loads the contents of a file to a list, representing the lines in the file
#
# @param s -> string -> path to the file to be read
# @return -> list -> list of the lines of the file
def loadFileToArray(s):
    outArr = []
    with open(s, 'r') as iFile:
        outArr = iFile.read().splitlines()

    return outArr

def zeroPad(cents):
    if len(cents) < 3:
        cents = cents.zfill(3)

    return cents

def validateAccountNumber(accountNumber, txCode=None):
    if txCode in ["NEW", "DEL", "WDR", "DEP"]:
        if accountNumber != "0000000":
            print beMessages.getMessage("invalidCustom",["account number for " + txCode,accountNumber])
            raise Exception
    else:
        if len(accountNumber) != 7 or accountNumber.startswith("0") or not isInt(accountNumber):
            print beMessages.getMessage("invalidCustom",["Account Number",accountNumber])
            raise Exception

def validateCentsAmount(centsAmount, txCode=None):
    if txCode in ["NEW", "DEL"]:
        if centsAmount != "000":
                print beMessages.getMessage("invalidCustom",["cents amount",centsAmount])
                raise Exception

    else:
        if not isInt(centsAmount) or len(centsAmount)  < 3 or len(centsAmount)  > 10:
            print beMessages.getMessage("invalidCustom",["cents amount",centsAmount])
            raise Exception

def validateAccountName(accountName, txCode=None):
    if txCode in ["WDR", "DEP", "XFR"]:
        if accountName != "***":
            print beMessages.getMessage("invalidCustom",["account name for " + txCode,accountName])
            raise Exception
    else:
        if len(accountName) < 3 or len(accountName) > 30 or accountName.startswith(" ") or accountName.endswith(" "):
            print beMessages.getMessage("invalidCustom",["account Name",accountName])
            raise Exception

def validateTransactionCode(code):
    if code not in ["NEW", "DEL", "WDR", "DEP", "XFR"]:
        print beMessages.getMessage("invalidCustom",["transaction code",code])
        raise Exception
