import messages

validSessionTypes = ["agent", "machine"]
loggedOutSessionType = "login"

def doLogin(currentSession, loginParam):
    if currentSession in validSessionTypes:
        # If the current session is in the valid list, then we don't need
        # to do anything
        print messages.getMessage("alreadyLoggedIn")
    else:
        if len(loginParam) < 2:
            print messages.getMessage("enterSessType")
        else:
            if loginParam[1] in validSessionTypes:
                # If the loginParam is valid, then we return it
                # This will log the user in
                return True, loginParam[1]
            else:
                # If the login param is invalid, print an error and return
                # the current session type (logged out)
                print messages.getMessage("invalidSess", loginParam[1])

    # We return the current session type (for invalid login types and
    # when the user is already logged in)
    return False, currentSession

def doLogout(currentSession):
    if currentSession in validSessionTypes:
        return loggedOutSessionType
    else:
        print messages.getMessage("alreadyLoggedOut")
