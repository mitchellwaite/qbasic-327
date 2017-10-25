import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_createacct1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct1_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_createacct1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/createacct/createacct1_transaction.txt"))

def test_createacct2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct2_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct2_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_createacct2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_createacct3(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct3_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct3_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_createacct3_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_createacct4(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/createacct/createacct4_input.txt',
                                macros.testDataDir() + '/frontend/createacct/createacct4_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_createacct4_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
