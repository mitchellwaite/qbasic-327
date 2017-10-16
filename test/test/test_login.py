import pytest
import pexpect
import os
import macros

mainPyCommand = "python {} -o {} -v {}/frontend/common/valid_accounts.txt".format(macros.mainPyLocation(), macros.testTempDir(), macros.testDataDir())
mydir = os.path.dirname(os.path.realpath(__file__))

@pytest.fixture
def setup():
   macros.removeTempDirs()

def run_test(child, input, output):
    child.sendline(input)
    idx = child.expect_exact([output,pexpect.TIMEOUT,pexpect.EOF],1)

    tmpLines = child.before.splitlines()
    actualOutput = tmpLines[len(tmpLines) - 2]

    if idx != 0:
        print "Error: expected output did not match actual output!\nCommand: {}\nExpected: {}\nActual: {}\n".format(input,output,actualOutput)

    return idx

def test_login(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login2_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login2_output.txt')]

    #print inputs
    #print outputs

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = pexpect.spawn(mainPyCommand)

    for i,o in combined:
        rc |= run_test(child,i,o)

    assert(rc == 0)
