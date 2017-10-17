import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_login1(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login1_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login1_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login2(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login2_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login2_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login3(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login3_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login3_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login4(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login4_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login4_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)

def test_login5(setup):
    rc = 0

    inputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login5_input.txt')]
    outputs = [line.strip() for line in open(macros.testDataDir() + '/frontend/login/login5_output.txt')]

    combined = []

    for i in range(0,len(inputs)):
        tmpTuple = [inputs[i], outputs[i]]
        combined.append(tmpTuple)

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    assert(rc == 0)
