import types

# List of message format strings, used for calls to the getMessage function
message = {
    "test": "this is a test",
    "masterAccountsLoc": "Loading old master accounts file from: {}",
    "mergedSummLoc": "Loading merged transaction summary from: {}",
    "outValidAccLoc": "Writing valid accounts list to: {}",
    "outMasterAccLoc": "Writing new master accounts file to: {}",
    "notImplemented": "{} has not been implemented yet.",
    "error": "Error returned from {} : {}",
    "invalidCustom": "Invalid {}: {}",
    "fatalError": "Fatal error returned from {} : {}",
    "fatalErrorLineLength": "Fatal error: Line {} of master accounts file is greater than 47 characters",
    "fatalErrorFieldCount": "Fatal error: The following line of the {} does not contain all required fields: \"{}\"",
    "msgErr": "message not found"
    }

# Selects the message from the above list, and applies the format string or
# list of format strings to the message, then returns it to the caller
#
# @param messageToGet -> string -> selects the message format string
# @param stringRep -> string or list of strings -> to apply to the message
# @return string -> formatted message
def getMessage(messageToGet, stringRep=[]):
    stringRepInt = None

    if messageToGet in message:
            if isinstance(stringRep,types.ListType):
                return message[messageToGet].format(*stringRep)
            elif isinstance(stringRep,types.StringTypes):
                return message[messageToGet].format(stringRep)
            else:
                stringRepInt = "Unknown message argument type: " + type(stringRep).__name__
                return stringRepInt
    else:
        return message["msgErr"]
