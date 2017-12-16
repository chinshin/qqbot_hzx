# -*- coding: utf-8 -*-
import setting
import json
import sys
import urllib3
import requests
# requests 要在urllib3之后import
reload(sys)
sys.setdefaultencoding('utf8')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


username = str(setting.user(1))
password = str(setting.user(2))


login_url = 'https://puser.48.cn/usersystem/api/user/v1/login/phone'
header = {
    'IMEI': '866716037825811',
    'User-Agent': 'Mobile_Pocket',
    'token': '0',
    'os': 'android',
    'version': '5.0.1',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '75',
    'Host': 'puser.48.cn',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}
params = {
    'latitude': 0,
    'longitude': 0,
    'password': password,
    'account': username,
}
response = requests.post(
    login_url,
    data=json.dumps(params),
    headers=header,
    verify=False
).json()
if response['status'] == 200:
    print 'token :  ', response['content']['token']
else:
    print 'error when get token\n', response
