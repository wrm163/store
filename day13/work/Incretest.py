import unittest
from day13.demo import Calculator


class TestCalc1(unittest.TestCase):

    def testIncre(self):
        c = Calculator()
        a = 6
        b = 3
        s = 3
        sum = c.Incre(a, b)
        self.assertEquals(s, sum)

    def testIncre1(self):
        c = Calculator()
        a = 6
        b = -3
        s = 9
        sum = c.Incre(a, b)
        self.assertEquals(s, sum)

    def testIncre2(self):
        c = Calculator()
        a = -6
        b = 3
        s = -9
        sum = c.Incre(a, b)
        self.assertEquals(s, sum)

    def testIncre3(self):
        c = Calculator()
        a = -6
        b = -3
        s = -3
        sum = c.Incre(a, b)
        self.assertEquals(s, sum)