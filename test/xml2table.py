from bs4 import BeautifulSoup
import sys

# Makes a nice table to look at in travis

resultTable = []

with open(sys.argv[1]) as fp:
    soup = BeautifulSoup(fp, "xml")

    suite = soup.find("testsuite")

    # <testsuite errors="0" failures="40" name="pytest" skips="0" tests="44" time="0.598">
    suTotal = suite["tests"]
    suPass = 0
    suFail = suite["failures"]
    suSkips = suite["skips"]
    suTime = suite["time"]




    for t in soup.find_all("testcase"):
        failures = t.find_all("failure")
        if len(failures) > 0:
            resultTable.append({ "file" : t["file"],
                                 "test" : t["name"],
                                 "line" : t["line"],
                                 "error": failures[0]["message"]})
        else:
            suPass += 1
            resultTable.append({ "file" : t["file"],
                                 "test" : t["name"],
                                 "line" : t["line"],
                                 "error": "Pass" })

print "QBasic Test Statistics:\n"
print "Pass: {}\nFail: {}\nTotal Tests: {}\nTime: {}s\n".format(suPass,suFail,suTotal,suTime)
print "Test Report:"

print "{:->31}|{:->32}|{:->6}|{:->25}".format("","","","")
print "{: <30} | {: <30} | {: <4} | {}".format("File", "Test", "Line", "Pass/Fail")
print "{:->31}|{:->32}|{:->6}|{:->25}".format("","","","")

for result in resultTable:
    print "{:<30} | {:<30} | {:<4} | {}".format(result["file"],result["test"], result["line"], result["error"])
