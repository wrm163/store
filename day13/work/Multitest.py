import unittest
from day13.demo import Calculator


class TestCalc2(unittest.TestCase):

    def testMulti(self):
        c = Calculator()
        a = 6
        b = 3
        s = 18
        sum = c.Multi(a, b)
        self.assertEquals(s, sum)

    def testMulti1(self):
        c = Calculator()
        a = 6
        b = -3
        s = -18
        sum = c.Multi(a, b)
        self.assertEquals(s, sum)

    def testMulti2(self):
        c = Calculator()
        a = -6
        b = 3
        s = -18
        sum = c.Multi(a, b)
        self.assertEquals(s, sum)

    def testMulti3(self):
        c = Calculator()
        a = -6
        b = -3
        s = 18
        sum = c.Multi(a, b)
        self.assertEquals(s, sum)