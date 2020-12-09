
import json
import requests
import jsonpath

session = requests.session()

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}
response = session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
response.encoding = response.apparent_encoding
v = response.json() #v就是对象
v1 = jsonpath.jsonpath( v, '$.access_token' )
print(v1)
v2 = jsonpath.jsonpath( v, '$.access_token' )[0]#加个0就是第一个元素 是字符串， 不是列表
print( v2 )
# value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]

# v2 = '{"access_token":"..."}'
# print( json.loads( v2 ) )
