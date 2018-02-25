import os
import time

project_path = [
       #note
       '/home/manue1/wiki/',
        ]


for path in project_path:
    os.chdir(path)
    cmd = "git add -A . && git commit -m '%d' && git push " % int(time.time())
    s = os.system(cmd)
    print "push %s status : %s" % (path.split('/')[-1],str(s))


