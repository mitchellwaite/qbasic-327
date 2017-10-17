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

def run_test(child, input, output):
    child.sendline(input)
    idx = child.expect_exact([output,pexpect.TIMEOUT,pexpect.EOF],1)

    tmpLines = child.before.splitlines()
    actualOutput = tmpLines[len(tmpLines) - 2]

    if idx != 0:
        print "Error: expected output did not match actual output!\nCommand: {}\nExpected: {}\nActual: {}\n".format(input,output,actualOutput)

    return idx
