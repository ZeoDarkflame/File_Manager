import subprocess
import tempfile

P = subprocess.Popen("dir",stdout=subprocess.PIPE,shell=True)
output,err = P.communicate()
#print(output.decode("utf-8"))
print(type(output))
print(type(output.decode('utf-8')))
l = output.decode('utf-8').splitlines()
l.pop(-1)
l.pop(-1)
for i in l:
    print(i)
print(l[3][14:])