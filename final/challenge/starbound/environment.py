#! /usr/bin/python

import subprocess
import os
import signal
import time
import sys
from subprocess import PIPE

targetProgram = '/home/starbound/starbound'

environ = {
	'TEST': 'hello',
	'PATH': '/home/starbound/bin',
	'ENV':	'/home/starbound/bin/.shrc',
	'SHELL': '/bin/sh',
	'LD_PRELOAD': '/home/starbound/isatty.so /home/starbound/hook.so'
}

p = subprocess.Popen(targetProgram, env=environ)


pid = str(p.pid)
while True:
	if p.poll() != None:
		sys.exit(0)
	p2 = subprocess.Popen('cat /proc/' + pid + '/environ', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out, err = p2.communicate()
	
	if 'PWD' in out or len(out) == 0:
		os.kill(p.pid, signal.SIGKILL)
		sys.exit(0)
		break
	time.sleep(0.5)

