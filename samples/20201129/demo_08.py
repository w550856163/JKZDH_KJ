# -*- coding: utf-8 -*-
#@File ：demo_08.py
#@Auth ： wwd
#@Time ： 2020/12/12 8:41 下午
import paramunittest
import unittest

@paramunittest.parametrized(
    (10,20),
    (30,40),
    # (100,20)
)
class ApiTestDemo(paramunittest.ParametrizedTestCase):  #unittest.TestCase
    def setParameters(self, numa,numb):
        self.a = numa
        self.b = numb
    def test_add_case(self):
        print( '%d+%d?=%d'%(self.a,self.b,30) )
        self.assertEqual( self.a + self.b,30 )

if __name__=='__main__':
    unittest.main(verbosity=2)
