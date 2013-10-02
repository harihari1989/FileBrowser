import os
import sys
import subprocess

path = sys.argv[0]
filename = sys.argv[1]
pathlist = []
for location in os.walk(path):
    if filename in location[-1]:
        file_index = location[-1].index(filename)
        pathlist.append(location[0]+'/'+location[-1][file_index])
cmd = 'dialog --menu "Select your file" 100 150 ' + str(len(pathlist))
i=1
for file in pathlist:
    cmd = cmd + ' ' + str(i) + ' ' +file
    i += 1
tmpfile = '~/tmp/tmp.txt'
cmd = cmd + ' 2>'+tmpfile
os.system(cmd)
cat_cmd = 'cat '+tmpfile
p = subprocess.Popen(cat_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
file_index = int(p.stdout.readlines()[0])
retval = p.wait()
os.system('rm '+tmpfile)
cmd = sys.argv[2] + ' ' + pathlist[file_index]
os.system(cmd)
