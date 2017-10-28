from bs4 import BeautifulSoup
import sys

# Makes a nice table to look at in travis, on the console, etc.

# Initialize an empty list
resultTable = []

with open(sys.argv[1]) as fp:
    # Parse the xml file with beautifulsoup
    soup = BeautifulSoup(fp, "xml")

    # Find the tag containing testsuite statistics
    suite = soup.find("testsuite")

    # Store the testsuite values
    # <testsuite errors="0" failures="40" name="pytest" skips="0" tests="44" time="0.598">
    suTotal = suite["tests"]
    suPass = 0
    suFail = suite["failures"]
    suSkips = suite["skips"]
    suTime = suite["time"]



    # Find all testcase entries
    for t in soup.find_all("testcase"):

        failures = t.find_all("failure")

        # If the testcase entry has a failure tag, append failure data to the list
        if len(failures) > 0:
            resultTable.append({ "file" : t["file"],
                                 "test" : t["name"],
                                 "line" : t["line"],
                                 "error": failures[0]["message"]})
        else:
            # If does not (test passed) add a "pass" to the list
            suPass += 1
            resultTable.append({ "file" : t["file"],
                                 "test" : t["name"],
                                 "line" : t["line"],
                                 "error": "Pass" })

# Print statistics
print "QBasic Test Statistics:\n"
print "Pass: {}\nFail: {}\nTotal Tests: {}\nTime: {}s\n".format(suPass,suFail,suTotal,suTime)
print "Test Report:"

# Print the table header
print "{:->31}|{:->32}|{:->6}|{:->25}".format("","","","")
print "{: <30} | {: <30} | {: <4} | {}".format("File", "Test", "Line", "Pass/Fail")
print "{:->31}|{:->32}|{:->6}|{:->25}".format("","","","")

# Print results to the table
for result in resultTable:
    print "{:<30} | {:<30} | {:<4} | {}".format(result["file"],result["test"], result["line"], result["error"])
