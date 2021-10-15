# use Popen to run terminal commands

from subprocess import Popen, PIPE
 
cmd = Popen(['df', '-h'], stdout=PIPE, stderr=PIPE)
stdout, stderr = cmd.communicate("")
