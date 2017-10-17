import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_logout1(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/logout/logout1_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/logout/logout1_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_logout1_txSummary():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt", macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
