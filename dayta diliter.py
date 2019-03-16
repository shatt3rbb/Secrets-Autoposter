import os,sys
import shutil

f = open("secret.json","w")
f.write("{")
f.write('\n')
f.write("}")
f.close()

f = open("rsa.pt","w")
f.write("{")
f.write('\n')
f.write("}")
f.close()

try:
    shutil.rmtree(os.path.dirname(sys.argv[0]) + "\\" + "__pycache__", ignore_errors=True)
except:
    print("The is no pycache folder to delete")