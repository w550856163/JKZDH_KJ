# -*- coding: utf-8 -*-
#@File ：requests_demo.py
#@Auth ： wwd
#@Time ： 2020/12/8 7:54 下午
import requests
session = requests.session()
get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}
response = session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
print( response.content.decode('utf-8') )

