# -*- coding: utf-8 -*-
#@File ：demo_07.py.py
#@Auth ： wwd
#@Time ： 2020/12/12 4:45 下午
import re
str1 = '{"access_token":"39_qHfCmB0GdutZ2MXC0G5IbzrM3WY7ES3JQF_bY04G-ceI-umT7_9E7-m0e3lVx-YFJRcTMnmKga-ijt45IFCrBPeIbbq0PsFphgzjAyaAeYhk8Po13Ix7oQQAi-a85xplVyuERp_rIci3wiP1CRKiAFAIXQ","expires_in":7200}'
str2 = '"access_token":"(.+?)kkk"'
v = re.findall(str2,str1)
if v :
    print( True )
else:
    print( False )
