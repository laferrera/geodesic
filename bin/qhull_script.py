import math
from subprocess import Popen, PIPE
import os
import os.path
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
QHULL_BUILD = os.path.join(SITE_ROOT, 'qhull-osx')

num_of_friends = 100
#for n in range(4, num_of_friends):
inc = math.pi * (3 - math.sqrt(5));
off = 2.0000 / num_of_friends;
hull_request_data =  "3\n" + str(num_of_friends) + "\n"
for i in range(0,num_of_friends):
    z = i * off - 1 + (off / 2);
    r = math.sqrt(1 - z*z);
    t =  i * inc;
    a = (r * math.cos(t));
    b = (r * math.sin(t));
    c = (z);
    hull_request_data += str(round(a,4)) +  " " + str(round(b,4)) +  " " + str(round(c,4)) + "\n";

#print hull_request_data
qhull = Popen([QHULL_BUILD, 'i'], bufsize=2048, stdin=PIPE)  
qhull.stdin.write(hull_request_data)
qhull.stdin.close();
#print qhull.check_output