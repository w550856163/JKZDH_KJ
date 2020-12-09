
a_dict = {'小红':[{'book1':'朝花夕拾'},{'book2':'红楼梦'}],
          '小黑':[{'book1':'呐喊'},{'book2':'红楼梦'}]}
data_list = []
for key,value in a_dict.items():#同时返回键和值，a_dict.key返回key,a_dict.value返回value
    b_dict = {}
    b_dict['name'] = key
    b_dict['books'] = value
    data_list.append(b_dict)
print( data_list )


