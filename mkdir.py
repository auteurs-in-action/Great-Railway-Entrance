import os

NARGS = 174
NISS = 149

for i in range(1,NISS+1):
    os.system("mkdir -p issue/%d" % i)
    os.system("touch issue/%d/placeholder" % i)
