import os,sys
import shutil


f = open("settings.midget","w")
f.write("json_file_name = ''")
f.write('\n')
f.write("fb_token = ''")
f.write('\n')
f.write("page_id = ''")
f.write('\n')
f.write("spreadsheet_name = ''")
f.write('\n')
f.close()

f = open("secret.json","w")
f.write("{")
f.write('\n')
f.write("}")
f.close()

try:
    shutil.rmtree(os.path.dirname(sys.argv[0]) + "\\" + "__pycache__", ignore_errors=True)
except:
    print("The is no pycache folder to delete")