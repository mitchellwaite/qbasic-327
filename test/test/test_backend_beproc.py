# FILE: test_backend_beproc.py
# DESC: Pytest testing harness for the QBasic backend functions
import pytest
import pexpect
import os
import sys
import macros

# Allows us to import the functions from beMod
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..' , 'src', 'backend'))
from beMod import *

# Decision coverage testing for the account creation transactions.
#
# The lines in the parametrize have the following syntax:
#   p1 -> inDict -> input dictionary representing the inital state of the internal master accounts file
#   p2 -> outDict -> output dictionary representing the expected final state of the internal master accounts file
#   p3 -> tx -> internal dict representation of the transaction we want to process
#
# The lines in the parametrize correspond to tests T1, T2, and T3 respectively:
#
# Decision    Master Accounts File Input  Merged Transaction Summary Input    Test
# 1: true     empty                       NEW 1234567 000 0000000 test        T1
# 1: false    empty                       DEP 1234567 123 0000000 ***         T2
# 2: true     1234567 123456 test         NEW 1234567 000 0000000 test        T3
@pytest.mark.parametrize("inDict,outDict,tx", [
    ({}, {'1234567': {'balance': 0, 'name': 'test'}},  {"code" : "NEW", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" }),
    ({}, {},  {"code" : "DEP", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "DEP 1234567 123 0000000 ***" }),
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 123456, 'name': 'test'}},  {"code" : "NEW", "amount" : "000", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "NEW 1234567 000 0000000 test" })
])
def test_runTransaction_new(inDict, outDict, tx):
    tmpOutDict = beProc.runTransaction(tx,inDict)
    assert outDict == tmpOutDict

# Statement coverage testing for the withdraw transactions.
#
# The lines in the parametrize have the following syntax:
#   p1 -> inDict -> input dictionary representing the inital state of the internal master accounts file
#   p2 -> outDict -> output dictionary representing the expected final state of the internal master accounts file
#   p3 -> tx -> internal dict representation of the transaction we want to process
#
# The lines in the parametrize correspond to tests T1 and T2 respectively:
#
# Statement   Master Accounts File Input  Merged Transaction Summary Input    Test
# 1           1234567 123456 test         WDR 1234567 1234 0000000 test       T1
# 1           1234567 123456 test         WDR 1234567 1234567 0000000 test    T2
@pytest.mark.parametrize("inDict,outDict,tx", [
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 122222, 'name': 'test'}},  {"code" : "WDR", "amount" : "1234", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "WDR 1234567 1234 0000000 ***" }),
    ({'1234567': {'balance': 123456, 'name': 'test'}}, {'1234567': {'balance': 123456, 'name': 'test'}},  {"code" : "WDR", "amount" : "1234567", "from" : "0000000", "to" : "1234567", "name" : "test", "str" : "WDR 1234567 1234567 0000000 ***" })
])
def test_runTransaction_wdr(inDict, outDict, tx):
    tmpOutDict = beProc.runTransaction(tx,inDict)
    assert outDict == tmpOutDict
