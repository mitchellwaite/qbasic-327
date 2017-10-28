import pytest
import pexpect
import os
import macros

# Pytest fixture, handles the initial conditions for each test.
# Clears the temporary directory, removing old summary files
@pytest.fixture
def setup():
   macros.removeTempDirs()

# Tests the login functionality, using login1_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_login1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login1_input.txt',
                                macros.testDataDir() + '/frontend/login/login1_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary directory for login1 is blank
def test_login1_noTxSummary():
    macros.assertEmptyTestDir()

# Tests the login functionality, using login2_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_login2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login2_input.txt',
                                macros.testDataDir() + '/frontend/login/login2_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of login2 is blank
def test_login2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Tests the login functionality, using login3_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_login3(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login3_input.txt',
                                macros.testDataDir() + '/frontend/login/login3_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of login3 is blank
def test_login3_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

# Tests the login functionality, using login4_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_login4(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login4_input.txt',
                                macros.testDataDir() + '/frontend/login/login4_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary directory from login4 is empty
def test_login4_noTxSummary():
    macros.assertEmptyTestDir()

# Tests the login functionality, using login5_input/output text files
#
# @param setup : pytest fixture at the top of the file, clears temp directory
#
# Returns: 0 for no error
# Throws:  AssertionError if any input/output tuple does not match what's expected
def test_login5(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login5_input.txt',
                                macros.testDataDir() + '/frontend/login/login5_output.txt')

    # Spawn the qbasic frontend
    child = macros.spawnFrontend()

    # Send each input, verify the response against the expected output
    # RC nonzero indicates a failed test
    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    # Check to see that we have passed all tests
    assert(rc == 0)

# Verifies that the transaction summary from the first session of login5 is blank
def test_login5_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
