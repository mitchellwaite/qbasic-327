import types

# List of message format strings, used for calls to the getMessage function
message = {
    "test": "this is a test",
    "notImplemented": "{} has not been implemented yet.",
    "unknownCommand": "Unknown Command: {}",
    "error": "Error returned from {} : {}",
    "fatalError": "Fatal QBasic error: {}",
    "msgErr": "message not found",
    "custValidPath": "Using valid accounts file found at: {}",
    "custTxPath": "Using transaction log path: {}",
    "invalidAcct": "{} is an invalid account",
    "accountAlreadyExists": "Could not create account. Account {} already exists.",
    "accountDoesntExist": "Could not complete transaction. Account {} doesn't exist.",
    "accountCreated": "Successfully created account #{}.",
    "accountDeleted": "Successfully deleted account #{}.",
    "pendingCreation": "Could not {}. Account {} is pending creation.",
    "pendingDeletion": "Could not {}. Account {} is pending deletion.",
    "enterSessType": "You must include a session type with the login command",
    "invalidSess": "Invalid session type: {}",
    "invalidCustom": "Invalid {}: {}",
    "mustBeAgent": "Insufficient permissions. You must be an agent to {}.",
    "loggedIn": "Logged in as {}.",
    "alreadyLoggedIn": "You are already logged in.",
    "alreadyLoggedOut": "You are already logged out.",
    "loggedOut": "Successfully logged out.",
    "txErrNotLoggedIn": "You must log in to run transactions.",
    "welcome": "Welcome to QBasic",
    "goodbye": "Thank you for using QBasic",
    "pleaseEnter": "Please enter {}",
    "depositSuccess": "Successfully deposit {} in to account #{}.",
    "transferSuccess": "Successfully transferred {} to account #{}.",
    "transferSameAccountError": "Could not transfer: 'From' and 'To' account numbers must be different.",
    "withdrawLimitErr": "Could not withdraw: the transaction would exceed the $1000 session limit for account #{}",
    "withdrawSuccess": "Successfully withdrew {} from account #{}"
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
