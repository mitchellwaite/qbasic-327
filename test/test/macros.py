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
    child = pexpect.spawn(frontendPyCommand);
    child.expect("> ") #Wait for a prompt
    return child;

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

    #Make sure the child is still alive.
    assert child.isalive()

    # Send the command
    child.sendline(input)

    # wait for a prompt again
    idx = child.expect(["> ",pexpect.TIMEOUT,pexpect.EOF])

    # this is the actual output from QBasic that we want
    spl = child.before.splitlines()
    #print spl
    actualOutput = spl[len(spl) - 1] #< right here.

    if output != actualOutput:
        print "Error: expected output did not match actual output!\nCommand: {}\nExpected: {}\nActual: {}\n".format(input,output,actualOutput)
        return -1
    else:
        return 0
