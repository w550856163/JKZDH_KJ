# -*- coding: utf-8 -*-
#@File ：demo_05.py
#@Auth ： wwd
#@Time ： 2020/12/11 1:14 上午
class Demo5:
    def __init__(self):
        self.function ={
            'json_key':self.key_check, #字符串对应函数
            'json_key_value': self.key_value_check
        }
    def key_check(self):
        print('key_check...')
    def key_value_check(self):
        print('key_value_check...')
    def run_check(self,check_type):
        self.function['json_key']()  #小括号表示调用key_check()的方法
if __name__=='__main__':
    demo5 = Demo5() #对象什么都不用传，里面是无参的构造。
    demo5.run_check('json_key')