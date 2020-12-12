# -*- coding: utf-8 -*-
#@File ：demo_10.py
#@Auth ： wwd
#@Time ： 2020/12/12 9:29 下午
import paramunittest
import unittest
test_data = [{'numa':10,'numb':30},{'numa':40,'numb':50}]
def get_data():
    return test_data
@paramunittest.parametrized(
    *get_data()
)
class ApiTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa, numb):
        self.a = numa
        self.b = numb
    def test_add(self):
        print('%d+%d?=%d' % (self.a, self.b, 40))
        self.assertEqual(self.a + self.b, 40)

if __name__=='__main__':
    unittest.main(verbosity=2)