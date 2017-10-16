import pytest
import pexpect

mainPyCommand = "python ../../src/main.py"

@pytest.fixture
def setup():
   print "setup fixture"

def test_login(setup):
   child = pexpect.spawn(mainPyCommand)
   
   child.sendline("lmao")

   idx = child.expect(['Unknown Command: lmao','(.*?)'])
   print child.before

   if child.isalive():
      child.close()

   print "index = {}".format(idx)

   assert(idx == 0)

def test_login_2(setup):
   assert(1==1)

def test_login_3(setup):
   raise ValueError
