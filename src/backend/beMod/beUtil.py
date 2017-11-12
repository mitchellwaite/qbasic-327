# FILE: beUtil.py
# DESC: Utility functions for QBasic backend components

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
    with open s as iFile:
        outArr = s.read().splitlines()

    return outArr

def validateAccountNumber(accountNumber, line, txCode=None):
    if len(accountNumber) != 7 or accountNumber.startswith("0") or not qbUtil.isInt(accountNumber):
        print messages.getMessage("invalidCustom",["Account Number",line])
        raise Exception

    if txCode in ["NEW", "DEL", "WDR", "DEP"]:
        if accountNumber != "***":
            print messages.getMessage("invalidCustom",["account name for " + txCode,line])
            raise Exception

def validateCentsAmount(centsAmount, line):
    if not qbUtil.isInt(centsAmount) or len(centsAmount < 3) or len(centsAmount > 10):
        print messages.getMessage("invalidCustom",["Cents amount",line])
        raise Exception

def validateAccountName(accountName, line, txCode=None):
    if len(accountName) < 3 or len(accountName) > 30 or accountName.startswith(" ") or accountName.endswith(" "):
        print messages.getMessage("invalidCustom",["Account Name",line])
        raise Exception

    if txCode in ["WDR", "DEP", "XFR"]:
        if accountName != "***":
            print messages.getMessage("invalidCustom",["account name for " + txCode,line])
            raise Exception

def validateTransactionCode(code, line):
    if code not in ["NEW", "DEL", "WDR", "DEP", "XFR"]:
        print messages.getMessage("invalidCustom",["transaction code",line])
        raise Exception
