import unittest
from day13.demo import Calculator

class TestCalc(unittest.TestCase):

    def testAdd(self):
        c = Calculator()
        a = 6
        b = 3
        s = 9
        sum = c.Add(a,b)
        self.assertEquals(s,sum)


    def testAdd1(self):
        c = Calculator()
        a = 6
        b = -3
        s = 3
        sum = c.Add(a, b)
        self.assertEquals(s, sum)

    def testAdd2(self):
        c = Calculator()
        a = -6
        b = 3
        s = -3
        sum = c.Add(a,b)
        self.assertEquals(s,sum)

    def testAdd3(self):
        c = Calculator()
        a = -6
        b = -3
        s = -9
        sum = c.Add(a,b)
        self.assertEquals(s,sum)