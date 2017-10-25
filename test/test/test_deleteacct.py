import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_deleteacct1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/deleteacct/deleteacct1_input.txt',
                                macros.testDataDir() + '/frontend/deleteacct/deleteacct1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_deleteacct1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/deleteacct/deleteacct1_transaction.txt"))

def test_deleteacct2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/deleteacct/deleteacct2_input.txt',
                                macros.testDataDir() + '/frontend/deleteacct/deleteacct2_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_deleteacct2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_deleteacct3(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/deleteacct/deleteacct3_input.txt',
                                macros.testDataDir() + '/frontend/deleteacct/deleteacct3_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_deleteacct3_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/deleteacct/deleteacct3_transaction.txt"))
