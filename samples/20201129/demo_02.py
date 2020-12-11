
# -*- coding: utf-8 -*-
#@File ：demo_02.py.py
#@Auth ： wwd
#@Time ： 2020/12/10 5:43 下午
import re
str2 ='{"tag":{"id":134,"name":"广东"}'
v=re.findall('"id":(.+?),',str2)[0]
print(v)