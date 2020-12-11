# -*- coding: utf-8 -*-
#@File ：check_utils.py
#@Auth ： wwd
#@Time ： 2020/12/10 7:18 下午
import requests
import json
import requests
import json

class CheckUtils:
    def __init__(self,response_data):
        self.response_data = response_data
        self.check_rules = {  #判断规则和方法名去对应的一个过程
            '无': self.none_check,
            'json_key': self.key_check,
            'json_key_value': self.key_value_check,
            '正则比对': self.regexp_check
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

    def key_check(self,check_data):
        print('111')
        key_list = check_data.split(',')
        tmp_result = []
        print(key_list)
        print(self.response_data.json().keys())
        for key in key_list:
            if key in self.response_data.json().keys():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            return self.fail_result
        else:
            return self.pass_result

    def key_value_check(self,check_data):
        key_value_dict = json.loads( check_data )
        tmp_result = []
        for key_value in key_value_dict.items():
            if key_value in self.response_data.json().items():
                tmp_result.append( self.pass_result )
            else:
                tmp_result.append( self.fail_result )
        if self.fail_result in tmp_result:
            return self.fail_result
        else:
            return self.pass_result

    def regexp_check(self,check_data):
        pass

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
    # print( checkUtils.key_check('access_token,expires_in') )
    # print( checkUtils.key_value_check('{"expires_in":7200}') )
    print( checkUtils.run_check('json_key','access_token,expires_in') )
    print( checkUtils.run_check('json_key_value','{"expires_in":7200}') )




