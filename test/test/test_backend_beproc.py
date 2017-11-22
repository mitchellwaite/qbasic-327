import pytest
import pexpect
import os
import sys
import macros

# Allows us to import the functions from
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..' , 'src', 'backend'))
from beMod import *


@pytest.mark.parametrize("inDict,outDict,tx", [
    ({}, {'1234567': {'balance': 0, 'name': 'test'}},  {"code" : "NEW", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" }),
    ({}, {},  {"code" : "DEP", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "DEP 1234567 123 0000000 ***" }),
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 123456, 'name': 'test'}},  {"code" : "NEW", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" })
])
def test_runTransaction_new(inDict, outDict, tx):
    tmpOutDict = beProc.runTransaction(tx,inDict)
    assert outDict == tmpOutDict

@pytest.mark.parametrize("inDict,outDict,tx", [
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 122222, 'name': 'test'}},  {"code" : "WDR", "amount" : "1234", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" }),
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 123456, 'name': 'test'}},  {"code" : "WDR", "amount" : "1234567", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" })
])
def test_runTransaction_wdr(inDict, outDict, tx):
    tmpOutDict = beProc.runTransaction(tx,inDict)
    assert outDict == tmpOutDict
