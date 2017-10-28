import shutil
import os
import pexpect
import filecmp
import difflib

# Returns the location of the main.py for the frontend
def mainPyLocation():
   return testHomeDir() + "/../src/main.py"

# Returns the path to the test "home" directory... essentially qbasic-327/test
def testHomeDir():
   return os.path.dirname(os.path.realpath(__file__)) + "/.."

# Returns the path to the data dir, containing the expected i/o files
def testDataDir():
   return testHomeDir() + '/data'

# Returns the path to the temp dir, used to store tx summary files for testing
def testTempDir():
   return testHomeDir() + '/tmp'

# Cleans up the temporary directory, makes a new one
def removeTempDirs():
   try:
       shutil.rmtree(testTempDir())
   except:
       pass

   os.makedirs(testTempDir())

# Reads in an input and expected output, returns a list of tuples
def getIoList(inFile, outFile):
    # Load both files
    inputs = [line.strip('\n').strip('\r') for line in open(inFile)]
    outputs = [line.strip('\n').strip('\r') for line in open(outFile)]

    # The inputs and outputs should be the same length! If not, throw an assert
    assert len(inputs) == len(outputs)

    combined = []

    # Create said list of tuples
    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    return combined

# Spawns the frontend using pexpect
def spawnFrontend():
    # Formats the command used to spawn the frontend, including the output dir and common valid accounts file
    frontendPyCommand = "python {} -o {} -v {}/frontend/common/valid_accounts.txt".format(mainPyLocation(), testTempDir(), testDataDir())

    # call pexpect to spawn the process
    child = pexpect.spawn(frontendPyCommand);

    #wait for a prompt, then return the child process to the caller
    child.expect("> ")
    return child;

# Compares two files. If they differ, print an error and the differences
def compare_files(file1, file2):
    result = filecmp.cmp(file1, file2)

    if result != True:
        print "Error: expected files did not match!\nFile 1: {}\nFile 2: {}\n".format(file1,file2)
        diff_files(file1, file2)

    return result

# Show the difference between two text files
def diff_files(file1, file2):
    # read both files in to lists
    with open(file1) as f:
        file1_lines = f.readlines()

    with open(file2) as f:
        file2_lines = f.readlines()

    # Using the differ library, diff the files
    d = difflib.Differ()
    diff = d.compare(file1_lines, file2_lines)

    # Print the result of the diff to the console
    print '\n'.join(diff)

# Checks to see if the temp directory is empty (useful for some tests)
def assertEmptyTestDir():
    assert os.listdir(testTempDir()) == []

# Checks an input and expected output against a child frontend process
def run_test(child, input, output):

    #Make sure the child is still alive.
    assert child.isalive()

    # Send the command
    child.sendline(input)

    # wait for a prompt again
    idx = child.expect(["> ",pexpect.TIMEOUT,pexpect.EOF])

    # Split the data that was returned
    spl = child.before.splitlines()

    # this is the actual output from QBasic that we want
    actualOutput = spl[len(spl) - 1] #< right here.

    # If they don't match, print an error and return -1
    if output != actualOutput:
        print "Error: expected output did not match actual output!\nCommand: {}\nExpected: {}\nActual: {}\n".format(input,output,actualOutput)
        return -1
    else:
        return 0
