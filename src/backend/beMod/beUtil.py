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

# Zero pads the input string to a minimum of three characters.
#
# @param s -> string -> string to pad
# @return -> string -> padded string
def zeroPad(s):
    if len(s) < 3:
        s = s.zfill(3)

    return s

# Validates that the account number is correctly formed.
# Prints a message and throws an exception if there's a problem
#
# @param accountNumber -> string -> account number to validate
def validateAccountNumber(accountNumber):
    if len(accountNumber) != 7 or accountNumber.startswith("0") or not isInt(accountNumber):
        print beMessages.getMessage("invalidCustom",["Account Number",accountNumber])
        raise Exception

# Validates that the account number for the "from" field is correctly formed.
# For single account transactions, it should be "0000000". For others, call
# the regular validateAccountNumber function
#
# Prints a message and throws an exception if there's a problem
#
# @param accountNumber -> string -> account number to validate
# @param txCode -> string -> transaction code, controls the validation criteria
def validateFromAccountNumber(accountNumber, txCode):
    # For NEW, DEL, WDR, DEP (single account) ensure the from account number is 0000000
    if txCode in ["NEW", "DEL", "WDR", "DEP"]:
        if accountNumber != "0000000":
            print beMessages.getMessage("invalidCustom",["account number for " + txCode,accountNumber])
            raise Exception
    # For XFR, call the regular validate function
    else:
        validateAccountNumber(accountNumber)

# Validates that an amount of cents is correctly formed. If a transaction code
# is specified, check that the amount is "000" for NEW and DEL transactions
#
# Prints a message and throws an exception if there's a problem
#
# @param centsAmount -> string -> cents amount to validate
# @param txCode (optional) -> string -> transaction code, controls the validation criteria
def validateCentsAmount(centsAmount, txCode=None):
    # for NEW and DEL, ensure the cents amount is "000"
    if txCode in ["NEW", "DEL"]:
        if centsAmount != "000":
                print beMessages.getMessage("invalidCustom",["cents amount",centsAmount])
                raise Exception
    # For other kinds of transactions...
    else:
        # Check that the string represents an integer, and it is between 3 and 10 digits
        if not isInt(centsAmount) or len(centsAmount)  < 3 or len(centsAmount)  > 10:
            print beMessages.getMessage("invalidCustom",["cents amount",centsAmount])
            raise Exception

# Validates that the account name is correctly formed. If a transaction code
# is specified, check that the name is "***" for WDR, DEP, and XFR
#
# Prints a message and throws an exception if there's a problem
#
# @param accountName -> string -> cents amount to validate
# @param txCode (optional) -> string -> transaction code, controls the validation criteria
def validateAccountName(accountName, txCode=None):
    # for WDR, DEP, and XFR, ensure the name is "***"
    if txCode in ["WDR", "DEP", "XFR"]:
        if accountName != "***":
            print beMessages.getMessage("invalidCustom",["account name for " + txCode,accountName])
            raise Exception
    # For other transactions, or if a code is not specified, ensure the account
    # name meets the constraints
    else:
        if len(accountName) < 3 or len(accountName) > 30 or accountName.startswith(" ") or accountName.endswith(" "):
            print beMessages.getMessage("invalidCustom",["account Name",accountName])
            raise Exception

# Validates that the transaction code is in an allowed list
#
# Prints a message and throws an exception if there's a problem
#
# @param code -> string -> transaction code to validate
def validateTransactionCode(code):
    if code not in ["NEW", "DEL", "WDR", "DEP", "XFR"]:
        print beMessages.getMessage("invalidCustom",["transaction code",code])
        raise Exception
