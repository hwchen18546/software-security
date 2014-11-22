import requests
import random

session = requests.Session()

url = 'http://tor.atdog.tw/'
get_response = requests.get(url)
print get_response.content
print get_response.headers

authenticity_token = get_response.content.split("<meta content=\"")[2]
authenticity_token = authenticity_token[0:44]
print authenticity_token 

get_response.headers['set-cookie'] = "netseer_cm=done; " + get_response.headers['set-cookie']
headers = {'Cookie': get_response.headers['set-cookie']}
print headers
post_data = {'user[username]': 'ggg', 'user[password]': '123456', 'authenticity_token': authenticity_token, 'commit': 'SignIn'}
post_response = session.post("http://tor.atdog.tw/users/login", data=post_data, headers=headers)
print post_response.content
 
