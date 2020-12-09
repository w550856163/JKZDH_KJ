import json
import ast
str1 = '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}'
print(type(str1))
# jsondata = json.loads(str1)
# print( type(jsondata) )
# dict1 = eval(str1)
dict1 = ast.literal_eval(str1)
print(dict1)
print(type(dict1))

# str2 = '3+3'
# c = ast.literal_eval(str2)
# print(c)