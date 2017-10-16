import shutil
import os

def mainPyLocation():
   return testHomeDir() + "/../src/main.py"

def testHomeDir():
   return os.path.dirname(os.path.realpath(__file__)) + "/.."

def testDataDir():
   return testHomeDir() + '/data'

def testTempDir():
   return testHomeDir() + '/tmp'

def removeTempDirs():
   try:
       shutil.rmtree(testTempDir())
   except Exception as e:
       pass

   os.makedirs(testTempDir())
