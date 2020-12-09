# # -*- coding: utf-8 -*-
# #@File ：requests_utils.py
# #@Auth ： wwd
# #@Time ： 2020/12/8 8:00 下午
# import jsonpath
# import requests
# import json
# from utils.config_utils import local_config
# import re
# class RequestsUtils:
#     def __init__(self):
#         self.hosts = local_config.HOSTS
#         self.session = requests.session()
#         self.tmp_variables={} #临时变量
#     def __get(self, requests_info):
#         url = self.hosts + requests_info['请求地址']# 取出下面字典中的请求地址。
# # {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': '无', '取值代码': '', '取值变量': '', '断言类型': 'body_regexp', '期望结果': '"access_token":"(.+?)"'}
#         variable_list = re.findall('\\${\w+}', requests_info['请求参数(get)'])
#         for variable in variable_list:
#             requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(variable,
#                                                                             '"%s"' % self.tmp_variables[variable[2:-1]])
#         response = self.session.get(url=url,
#                                    params=json.loads(requests_info['请求参数(get)']),
#                                    headers=requests_info['请求头部信息'])
#         if requests_info['取值方式'] == 'jsonpath取值':
#             value = jsonpath.jsonpath(response.json(), requests_info['取值代码'])[0]
#             self.tmp_variables[requests_info['取值变量']] = value
#     #取值变量就是token ,value就是用正则表达式真正提取出来的一个值，放在一个字典里面成为一个真正的键值对，变量名就是临时字典key的名字
#         result = {
#             'code':0,
#             'response_code':response.status_code,
#             'response_reason':response.reason,
#             'response_headers':response.headers,
#             'response_body':response.text
#         }
#         return result
#
#     def __post(self, requests_info):
#         url = self.hosts + requests_info['请求地址']
#         get_variable_list = re.findall('\\${\w+}', requests_info['请求参数(get)'])
#         for variable in get_variable_list:
#             requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(variable,
#                                                                             '"%s"' % self.tmp_variables[variable[2:-1]])
#
#         post_variable_list = re.findall('\\${\w+}', requests_info['请求参数(post)'])  #取tag_id
#         for variable in post_variable_list:
#             requests_info['请求参数(post)'] = requests_info['请求参数(post)'].replace(variable,
#                                                                               '"%s"' % self.tmp_variables[
#                                                                                   variable[2:-1]])
#         response = self.session.post(url=url,
#                                  headers=requests_info['请求头部信息'],
#                                  params=json.loads(requests_info['请求参数(get)']),
#                                  json=json.loads(requests_info['请求参数(post)'])
#                                  )#参数名 =参数值
#         response.encoding = response.apparent_encoding#防止乱码
#         if requests_info['取值方式'] == 'jsonpath取值':
#                   value = jsonpath.jsonpath(response.json(), requests_info['取值代码'])[0]
#                   self.tmp_variables[requests_info['取值变量']] = value
#         result = {
#             'code': 0,
#             'response_code': response.status_code,
#             'response_reason': response.reason,
#             'response_headers': response.headers,
#             'response_body': response.text
#         }
#         return result
#
#     def request(self, step_info):
#         request_type = step_info['请求方式']
#         if request_type == "get":
#             result = self.__get(step_info)
#         elif request_type == "post":
#             result = self.__post(step_info)
#         else:
#             result = {'code': 1, 'result': '请求方式不支持'}
#         print(self.tmp_variables)
#         return result
#
#     def request_by_step(self, test_steps):
#         for test_step in test_steps:
#             result = self.request(test_step)
#             if result['code'] != 0:
#                 break
#             print(result['response_body'])
#         return result
# # if __name__=='__main__':    # 测试封装的get（）方法
# #         req_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': '无', '取值代码': '', '取值变量': '', '断言类型': 'body_regexp', '期望结果': '"access_token":"(.+?)"'}
# #         requestsUtils = RequestsUtils()
# #         v = requestsUtils.get(req_dict)
# #         print(v)
# #
# # if __name__ == '__main__':# 测试封装的post（）方法
# #         req_post_dict = {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":"39_ZlzNDPma7qLWpLJ4K0ir_cSahJ_fg9aevBpGvqRp9VNjqRE6hSkBOSUFla-mFjSGKyF-YFx28sM4Ch1rJISPGVSTahZ8l_xQ9M7CnAFoqUfibusAdeOI4lHEIzB6zhXJQHN5b9as9zhcGtSbBYKeAGAEBN"}', '请求参数(post)': '{   "tag":{        "id" : 456   } }'}
# #         requestsUtils = RequestsUtils()
# #         v = requestsUtils.post( req_post_dict)
# #         print( v )
#
# if __name__=='__main__': #不用直接封装get和post获取
#         # req_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': '无', '取值代码': '', '取值变量': '', '断言类型': 'body_regexp', '期望结果': '"access_token":"(.+?)"'}
#         # requestsUtils = RequestsUtils()
#         # v = requestsUtils.request(req_dict)
#         # print(v)
#         step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{   "tag" : {     "name" : "p3p4hehehe123" } } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
#
#         requestsUtils = RequestsUtils()
#         r = requestsUtils.request_by_step(step_list)
#         # print( r['response_body'] )
import json
import jsonpath
import requests
import re
from utils.config_utils import local_config

class RequestsUtils:
    def __init__(self):
        self.hosts = local_config.HOSTS
        self.session = requests.session()
        self.tmp_variables={}
    def __get(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        variable_list = re.findall('\\${\w+}',requests_info['请求参数(get)'])
        for variable in variable_list:
            requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(variable,
                                        '"%s"'%self.tmp_variables[variable[2:-1]])
        response = self.session.get( url = url,
                                     params = json.loads(requests_info['请求参数(get)']),
                                     headers = requests_info['请求头部信息'])
        response.encoding = response.apparent_encoding #保证不乱码
        if requests_info['取值方式'] == 'jsonpath取值':
            value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result = {
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def __post(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        get_variable_list = re.findall('\\${\w+}', requests_info['请求参数(get)'])
        for variable in get_variable_list:
            requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(variable,
                                        '"%s"'%self.tmp_variables[variable[2:-1]])
        post_variable_list = re.findall('\\${\w+}', requests_info['请求参数(post)'])
        for variable in post_variable_list:
            requests_info['请求参数(post)'] = requests_info['请求参数(post)'].replace(variable,
                                            '"%s"'%self.tmp_variables[variable[2:-1]])
        response = self.session.post(url=url,
                                     headers=requests_info['请求头部信息'],
                                     params=json.loads(requests_info['请求参数(get)']),
                                     json = json.loads(requests_info['请求参数(post)'])
                                    )
        response.encoding = response.apparent_encoding
        if requests_info['取值方式'] == 'jsonpath取值':
            value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result = {
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code':1,'result':'请求方式不支持'}
        print(self.tmp_variables)
        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result = self.request(test_step)
            if result['code'] != 0:
                break
            print(result['response_body'])
        return result




if __name__=='__main__':
    # req_post_dict = {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":"39_ZlzNDPma7qLWpLJ4K0ir_cSahJ_fg9aevBpGvqRp9VNjqRE6hSkBOSUFla-mFjSGKyF-YFx28sM4Ch1rJISPGVSTahZ8l_xQ9M7CnAFoqUfibusAdeOI4lHEIzB6zhXJQHN5b9as9zhcGtSbBYKeAGAEBN"}', '请求参数(post)': '{   "tag":{        "id" : 456   } }'}
    # req_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': ''}

    # step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': ''}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":"39_Bm5UI-zvWkokwnl6d3zCW30hk3sVHSv6sh6cHN3dbgnwUdfmhM-EFZ3OIrTechkzaRt9Iae3yX_MF7_h7bobNybvkoAC1CM2pAfGfNqSegXsPbjyJzkgSHtBV1OezPwEvFn60jS3__w5BdzVMRHcAHAYDT"}', '请求参数(post)': '{   "tag" : {     "name" : "广东" } } '}]
    # requestsUtils = RequestsUtils()
    # requestsUtils.request_by_step( step_list )
    # print( v )

    step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{   "tag" : {     "name" : "p3p4hehehe1" } } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    #step_list = [{'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '请求参数(post)': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'}, {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{   "tag" : {     "name" : "p3p4pppp2" } } ', '取值方式': 'jsonpath取值', '取值代码': '$.tag.id', '取值变量': 'tag_id'}, {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{"tag":{"id":${tag_id}}}', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    requestsUtils = RequestsUtils()
    r = requestsUtils.request_by_step(step_list)
    # print( r['response_body'] )
