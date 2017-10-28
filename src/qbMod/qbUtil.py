# FILE: qbUtil.py
# DESC: Utility functions for other QBasic components

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

# Converts a string representation of cents to dollars
#
# @param cents -> string -> value to convert
# @return string -> converted value
def centsToDollars(cents):
    if len(cents) < 3:
        cents = cents.zfill(3)

    return "$" + cents[:-2] + "." + cents[-2:]
