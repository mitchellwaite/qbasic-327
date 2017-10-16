message = {
    "test" : "this is a test",
    "notImplemented" : "{} has not been implemented yet.",
    "unknownCommand" : "Unknown Command: {}",
    "error" : "Error returned from {} : {}",
    "msgErr" : "message not found",
    "invalidAcct" : "{} is an invalid account",
    "enterSessType" : "You must include a session type with the login command",
    "invalidSess" : "Invalid session type: {}",
    "loggedIn"    : "Logged in as {}.",
    "alreadyLoggedIn" : "You are already logged in.",
    "alreadyLoggedOut" : "You are already logged out.",
    "loggedOut"   : "Successfully logged out.",
    "txErrNotLoggedIn" : "You must log in to run transactions.",
    "welcome" : "Welcome to QBasic",
    "goodbye" : "Thank you for using QBasic"
}



def getMessage(messageToGet, stringRep=[]):
    if messageToGet in message:
        return message[messageToGet].format(stringRep)
    else:
        return message["msgErr"]
