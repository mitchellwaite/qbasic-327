import pytest
import pexpect
import os
import macros

# Pytest fixture, handles the initial conditions for each test.
# Clears the temporary directory, removing old summary files
@pytest.fixture
def setup():
   macros.removeTempDirs()

# Tests the createacct functionality, using createacct1_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_createacct1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct1_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct1_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Close QBasic
    child.close()

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of createacct matches the one provided
def test_createacct1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/createacct/createacct1_transaction.txt"))

# Tests the createacct functionality, using createacct2_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_createacct2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct2_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct2_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Close QBasic
    child.close()

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of createacct2 is blank
def test_createacct2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Tests the createacct functionality, using createacct3_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_createacct3(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct3_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct3_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Close QBasic
    child.close()

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of createacct3 is blank
def test_createacct3_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Tests the createacct functionality, using createacct2_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_createacct4(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct4_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct4_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Close QBasic
    child.close()

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of createacct4 is blank
def test_createacct4_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
