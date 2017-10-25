import shutil
import os
import pexpect
import filecmp
import difflib
#from difflib_data import *


def mainPyLocation():
   return testHomeDir() + "/../src/main.py"

def testHomeDir():
   return os.path.dirname(os.path.realpath(__file__)) + "/.."

def testDataDir():
   return testHomeDir() + '/data'

def testTempDir():
   return testHomeDir() + '/tmp'

def removeTempDirs():
   try:
       shutil.rmtree(testTempDir())
   except:
       pass

   os.makedirs(testTempDir())

def getIoList(inFile, outFile):
    inputs = [line.strip('\n').strip('\r') for line in open(inFile)]
    outputs = [line.strip('\n').strip('\r') for line in open(outFile)]

    # The inputs and outputs should be the same length!
    assert len(inputs) == len(outputs)

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    return combined

def spawnFrontend():
    frontendPyCommand = "python {} -o {} -v {}/frontend/common/valid_accounts.txt".format(mainPyLocation(), testTempDir(), testDataDir())
    return pexpect.spawn(frontendPyCommand)

def compare_files(file1, file2):
    result = filecmp.cmp(file1, file2)

    if result != True:
        print "Error: expected files did not match!\nFile 1: {}\nFile 2: {}\n".format(file1,file2)
        diff_files(file1, file2)

    return result

def diff_files(file1, file2):
    with open(file1) as f:
        file1_lines = f.readlines()

    with open(file2) as f:
        file2_lines = f.readlines()

    d = difflib.Differ()
    diff = d.compare(file1_lines, file2_lines)
    print '\n'.join(diff)

def assertEmptyTestDir():
    assert os.listdir(testTempDir()) == []

def run_test(child, input, output):

    if not child.isalive():
        print "Error: child is dead."
        return -1

    # Wait for a prompt.
    idx = child.expect_exact([">",pexpect.TIMEOUT,pexpect.EOF],1)

    # Send the command
    child.sendline(input)

    # this is a dummy readline, it throws away the sendline from above
    child.readline()

    # this is the actual output from QBasic that we want
    actualOutput = child.readline().rstrip()

    if output != actualOutput:
        print "Error: expected output did not match actual output!\nCommand: {}\nExpected: {}\nActual: {}\n".format(input,output,actualOutput)
        return -1
    else:
        return 0
