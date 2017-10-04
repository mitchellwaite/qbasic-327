import pytest

@pytest.fixture
def setup():
   print "setup fixture"

def test_login(setup):
   assert(0==0)

def test_login_2(setup):
   assert(1==1)

def test_login_3(setup):
   raise ValueError
