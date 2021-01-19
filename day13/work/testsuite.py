import unittest
from work.addtest import TestCalc
from  work.Incretest import TestCalc1
from work.Multitest import TestCalc2
from work.Dividtest import TestCalc3
from HTMLTestRunner import HTMLTestRunner
import os

suite = unittest.TestSuite()

tests = unittest.defaultTestLoader.discover(os.getcwd(),"*test.py")
suite.addTest(tests)

f = open("计算器的测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity=1,
    title="计算器的测试报告"
)
runner.run(suite)