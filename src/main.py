#!/usr/bin/env python
import sys, getopt, os
import readline
from qbMod import *




def main():

    #control variables
    mainLoop = True;
    sessionType = "login"

    # Account list and transaction files
    validAccountsList = []
    transactionList = []
    validAccoutsListPath = "./validaccounts.txt"
    transactionListPath = "./out"

    # Set up parameters, so we can customize the locations of the inputs/outputs
    try:
        opts, args = getopt.getopt(sys.argv[1:],"v:o:")

        for opt, arg in opts:
            if opt == "-v":
                #Path to the valid accounts file
                validAccoutsListPath = arg
                print messages.getMessage("custValidPath", arg)
            elif opt == "-o":
                #Path to the place we want to store the transaction lists
                transactionListPath = arg
                print messages.getMessage("custTxPath", arg)
    except Exception as e:
        mainLoop = False
        print messages.getMessage("fatalError",str(e))
        return -1

    if not os.path.exists(transactionListPath):
        os.makedirs(transactionListPath)

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
                    print messages.getMessage("loggedIn",sessionType)

            elif command == "logout":
                    logoutSuccess = session.doLogout(sessionType)

                    if logoutSuccess:
                        # if the logout was successful, we neet to write a tx file
                        # and set the session type
                        tx.writeTransactionList([],transactionListPath)

                        print messages.getMessage("loggedOut",sessionType)
                        sessionType = session.loggedOutSessionType

            elif command in ["createacct","deleteacct","deposit","withdraw","transfer"]:
                print messages.getMessage("notImplemented", command)
            else:
                print messages.getMessage("unknownCommand", command)
        except KeyboardInterrupt:
            mainLoop = False
        except EOFError:
            mainLoop = False

    print messages.getMessage("goodbye")

if __name__ == "__main__":
    main()
