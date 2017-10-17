import messages

loggedOutSessionType = "login"
privilegedSessionType = "agent"

validSessionTypes = [privilegedSessionType, "machine"]

def doLogin(currentSession):
    if currentSession in validSessionTypes:
        # If the current session is in the valid list, then we don't need
        # to do anything
        print messages.getMessage("alreadyLoggedIn")
    else:
        print messages.getMessage("pleaseEnter","session type")
        sessionType = raw_input("> ")

        if sessionType in validSessionTypes:
            # If the loginParam is valid, then we return it
            # This will log the user in
            return True, sessionType
        else:
            # If the login param is invalid, print an error and return
            # the current session type (logged out)
            print messages.getMessage("invalidSess", sessionType)

    # We return the current session type (for invalid login types and
    # when the user is already logged in)
    return False, currentSession

def doLogout(currentSession):
    if currentSession in validSessionTypes:
        return loggedOutSessionType
    else:
        print messages.getMessage("alreadyLoggedOut")
