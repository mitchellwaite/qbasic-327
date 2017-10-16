#!/usr/bin/env python
import sys
import readline
from qbMod import *


validAccountsList = []
transactionList = []

def main():

    #control variables
    mainLoop = True;
    sessionType = "login"

    print messages.getMessage("welcome")

    while mainLoop:
        try:
            inputArgs = raw_input("{}> ".format(sessionType)).split(" ")
            command = inputArgs[0]

            if command == "quit":
                mainLoop = False
            elif command == "login":
                loginSuccess, loginSessionType = session.doLogin(sessionType, inputArgs)

                if loginSuccess:
                    # if the login was successful, we need to read the valid
                    # accounts file and set the session type
                    sessionType = loginSessionType

            elif command == "logout":
                    logoutSuccess = session.doLogout(sessionType)

                    if logoutSuccess:
                        # if the logout was successful, we neet to write a tx file
                        # and set the session type
                        sessionType = session.loggedOutSessionType
            elif command in ["createacct","deleteacct","deposit","withdraw","transfer"]:
                print messages.getMessage("notImplemented", command)
            else:
                print messages.getMessage("unknownCommand", command)
        except KeyboardInterrupt:
            mainLoop = False

    print messages.getMessage("goodbye")

if __name__ == "__main__":
    main()
