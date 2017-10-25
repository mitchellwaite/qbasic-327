import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_login1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login1_input.txt',
                                macros.testDataDir() + '/frontend/login/login1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login1_noTxSummary():
    macros.assertEmptyTestDir()

def test_login2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login2_input.txt',
                                macros.testDataDir() + '/frontend/login/login2_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login2_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_login3(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login3_input.txt',
                                macros.testDataDir() + '/frontend/login/login3_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login3_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))


def test_login4(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login4_input.txt',
                                macros.testDataDir() + '/frontend/login/login4_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login4_noTxSummary():
    macros.assertEmptyTestDir()

def test_login5(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/login/login5_input.txt',
                                macros.testDataDir() + '/frontend/login/login5_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login5_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
