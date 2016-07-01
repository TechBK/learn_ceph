import shlex
import subprocess
command_line = "ls -l"

args = shlex.split(command_line)
print args
p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # Success!
print p.communicate()