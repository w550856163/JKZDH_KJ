# -*- coding: utf-8 -*-
#@File ：demo_09.py
#@Auth ： wwd
#@Time ： 2020/12/12 9:08 下午
import paramunittest
import unittest
@paramunittest.parametrized(
    {'numa':10,'numb':30},
    {'numa':40,'numb':50}
)
class ApiTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa ,numb):
        self.a =numa
        self.b=numb

    def test_add_case(self):
        print('%d+%d?=%d' % (self.a, self.b, 40))
        self.assertEqual(self.a + self.b, 40)

if __name__ =='__main__':
    unittest.main(verbosity=2)