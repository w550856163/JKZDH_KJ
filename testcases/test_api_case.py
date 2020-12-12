# -*- coding: utf-8 -*-
#@File ：test_api_case.py
#@Auth ： wwd
#@Time ： 2020/12/12 11:49 下午
import os
import unittest
import warnings
import paramunittest
from utils.testcase_data_utils import TestcaseDataUtils
from utils.requests_utils import RequestsUtils

test_case_lists = TestcaseDataUtils().convert_testcase_data_to_list()

@paramunittest.parametrized(
    *test_case_lists
)
class TestApiCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
    def setParameters(self, case_id, case_step):
        self.case_id = case_id,
        self.case_step = case_step
    def test_api_case(self):
        self._testMethodName = self.case_step[0].get('测试用例编号')
        self._testMethodDoc = self.case_step[0].get('测试用例名称')
        test_result = RequestsUtils().request_by_step(self.case_step)
        self.assertTrue( test_result['check_result'] )

if __name__=='__main__':
    unittest.main(verbosity=2)
