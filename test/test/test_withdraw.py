import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_withdraw1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/withdraw/withdraw1_input.txt',
                                macros.testDataDir() + '/frontend/withdraw/withdraw1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_withdraw1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw1_transaction_0.txt"))

def test_withdraw1_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw1_transaction_1.txt"))

def test_withdraw2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/withdraw/withdraw2_input.txt',
                                macros.testDataDir() + '/frontend/withdraw/withdraw2_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_withdraw2_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_withdraw2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/withdraw/withdraw2_transaction.txt"))
