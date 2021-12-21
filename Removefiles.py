import os
import time
import shutil

path=""
days=30
seconds=time.time(days)
if os.path.exists(path):
  os.walk(path)
  os.path.join()
  ctime=os.stat(path).st_ctime
  if ctime>days:
    os.remove(path)
    shutil.rmtree(path)
else:
  print("not found")
