import shlex
import subprocess
command_line = "ssh ceph1 sudo rbd export-diff --from-snap snap2 pool1/img1@snap1 - | ssh ceph2 sudo rbd import-diff -"

args = shlex.split(command_line)
print args
p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # Success!
print p.communicate()