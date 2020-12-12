# -*- coding: utf-8 -*-
#@File ：check_utils.py
#@Auth ： wwd
#@Time ： 2020/12/10 7:18 下午
import requests
import json
import re
class CheckUtils:
    def __init__(self,response_data):
        self.response_data = response_data
        self.check_rules = {  #判断规则和方法名去对应的一个过程
            'none': self.none_check,
            'json_key': self.body_key_check,   #'json_key': self.key_check,
            'json_key_value': self.body_key_value_check,    #'json_key_value':self.key_value_check,
            'body_regexp': self.regexp_check,
            'header_key': self.header_key_check,#比对响应头
            'header_key_value': self.header_key_value_check, #比对响应头和它对应的值
            'response_code': self.response_code_check

        }
        self.pass_result = {
            'code':0, # 状态吗，0表示断言成功
            'response_code':self.response_data.status_code,
            'response_reason':self.response_data.reason,
            'response_headers':self.response_data.headers,
            'response_body':self.response_data.text,
            'response_url':self.response_data.url,
            'check_result': True
        }
        self.fail_result = {
            'code':1,
            'response_code':self.response_data.status_code,
            'response_reason':self.response_data.reason,
            'response_headers':self.response_data.headers,
            'response_body':self.response_data.text,
            'response_url':self.response_data.url,
            'check_result': False
        }

    def none_check(self):
        return self.pass_result

    def __key_check(self,actual_result,check_data):  #做成公共的私有的内置方法
        #print('111')
        key_list = check_data.split(',')
        tmp_result = []
        #print(key_list)
        #print(self.response_data.json().keys())
        for key in key_list:
            if key in actual_result.keys():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            return self.fail_result
        else:
            return self.pass_result

    def header_key_check(self,check_data): #检查头部的
        return self.__key_check(self.response_data.headers,check_data)
    def body_key_check(self,check_data): #检查正文的
        return self.__key_check(self.response_data.json(),check_data)

    def __key_value_check(self,actual_result,check_data):
        key_value_dict = json.loads( check_data )
        tmp_result = []
        for key_value in key_value_dict.items():
            if key_value in actual_result.items():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            return self.fail_result
        else:
            return self.pass_result
    def header_key_value_check(self,check_data):
        return self.__key_value_check(self.response_data.headers,check_data)
    def body_key_value_check(self,check_data):
        return self.__key_value_check(self.response_data.json(),check_data) #这里需要json因为是键值对

    def response_code_check(self,check_data):
        if self.response_data.status_code == int(check_data):
            return self.pass_result
        else:
            return self.fail_result

    def regexp_check(self, check_data):
        tmp_result = re.findall(check_data, self.response_data.text)#这里需要字符串/txt
        if tmp_result:
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,check_type,check_data):
        if check_type=='无' or check_data == '':
            return self.check_rules[check_type]()
        else:
            return self.check_rules[check_type](check_data)

if __name__=='__main__':
    session = requests.session()
    get_param_dict = {
        "grant_type": "client_credential",
        "appid": "wx55614004f367f8ca",
        "secret": "65515b46dd758dfdb09420bb7db2c67f"
    }
    response = session.get(url='https://api.weixin.qq.com/cgi-bin/token',
                           params=get_param_dict)
    response.encoding = response.apparent_encoding
    checkUtils = CheckUtils(response)
    print(response.headers)
    # print( checkUtils.key_check('access_token,expires_in') )
    # print( checkUtils.key_value_check('{"expires_in":7200}') )
    print( checkUtils.run_check('json_key','access_token,expires_in') )
    print( checkUtils.run_check('json_key_value','{"expires_in":7200}') )
    print(checkUtils.run_check('body_regexp', '"access_token":"(.+?)ss"'))
    print(checkUtils.run_check('header_key', 'Connection,Content-Length'))
    print( checkUtils.run_check('header_key_value','{"Connection":"keep-alive"}') )#键值对



