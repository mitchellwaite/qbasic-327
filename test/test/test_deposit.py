import pytest
import pexpect
import os
import macros

# Pytest fixture, handles the initial conditions for each test.
# Clears the temporary directory, removing old summary files
@pytest.fixture
def setup():
   macros.removeTempDirs()

# Tests the deposit functionality, using deposit1_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_deposit1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/deposit/deposit1_input.txt',
                                macros.testDataDir() + '/frontend/deposit/deposit1_output.txt')

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

# Verifies that the transaction summary from the first session of deposit1 matches the one provided
def test_deposit1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/deposit/deposit1_transaction_0.txt"))

# Verifies that the transaction summary from the second session of deposit1 matches the one provided
def test_deposit1_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/deposit/deposit1_transaction_1.txt"))

# Tests the deposit functionality, using deposit2_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_deposit2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/deposit/deposit2_input.txt',
                                macros.testDataDir() + '/frontend/deposit/deposit2_output.txt')

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

# Verifies that the transaction summary from the first session of deposit2 is blank
def test_deposit2_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Verifies that the transaction summary from the second session of deposit2 is blank
def test_deposit2_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
