import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_logout1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/logout/logout1_input.txt',
                                macros.testDataDir() + '/frontend/logout/logout1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_logout1_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt", macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_logout1_noTxSummary():
    assert os.listdir(macros.testTempDir()).length == 0
