import pytest
import pexpect
import os
import macros

# Pytest fixture, handles the initial conditions for each test.
# Clears the temporary directory, removing old summary files
@pytest.fixture
def setup():
   macros.removeTempDirs()

# Tests the withdraw functionality, using withdraw1_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_withdraw1(setup):
    rc = 0

    # Read the inputs and outputs in to a list of tuples
    combined = macros.getIoList(macros.testDataDir() + '/frontend/withdraw/withdraw1_input.txt',
                                macros.testDataDir() + '/frontend/withdraw/withdraw1_output.txt')

    # Spawn the Qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Close QBasic
    child.close()

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of withdraw1 matches the one provided
def test_withdraw1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw1_transaction_0.txt"))

# Verifies that the transaction summary from the second session of withdraw1 matches the one provided
def test_withdraw1_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw1_transaction_1.txt"))

# Tests the withdraw functionality, using withdraw2_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_withdraw2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/withdraw/withdraw2_input.txt',
                                macros.testDataDir() + '/frontend/withdraw/withdraw2_output.txt')

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

# Verifies that the transaction summary from the first session of withdraw2 is blank
def test_withdraw2_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Verifies that the transaction summary from the second session of withdraw2 matches the one provided
def test_withdraw2_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw2_transaction.txt"))
