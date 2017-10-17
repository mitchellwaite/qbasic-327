def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def centsToDollars(cents):
    return "$" + cents[:-2] + "." + cents[-2:]
