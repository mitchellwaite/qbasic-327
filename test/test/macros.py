import shutil
import os

def removeTempDirs():
   try:
       shutil.rmtree("../tmp")
   except Exception as e:
       pass

   os.makedirs("../tmp")
