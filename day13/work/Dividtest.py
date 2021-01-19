import unittest
from day13.demo import Calculator


class TestCalc3(unittest.TestCase):

    def testDivid(self):
        c = Calculator()
        a = 6
        b = 3
        s = 2
        sum = c.Divid(a, b)
        self.assertEquals(s, sum)

    def testDivid1(self):
        c = Calculator()
        a = 6
        b = -3
        s = -2
        sum = c.Divid(a, b)
        self.assertEquals(s, sum)

    def testDivid2(self):
        c = Calculator()
        a = -6
        b = 3
        s = -2
        sum = c.Divid(a, b)
        self.assertEquals(s, sum)

    def testDivid3(self):
        c = Calculator()
        a = -6
        b = -3
        s = 2
        sum = c.Divid(a, b)
        self.assertEquals(s, sum)