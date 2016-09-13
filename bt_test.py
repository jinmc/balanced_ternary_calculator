from bt import *
import unittest

class Testbt(unittest.TestCase):

    def setUp(self):
        store('0')
    
    def test_add(self):
        add('10')
        self.assertEqual(memory_as_int(), 3)

    def test_subtract(self):
        subtract('10')
        self.assertEqual(memory_as_int(), -3)

    def test_multiply(self):
        add('10')
        multiply('10')
        self.assertEqual(memory_as_int(), 9)

    def test_divide(self):
        add('100')
        divide('10')
        self.assertEqual(memory_as_int(), 3)

    def test_remainder(self):
        add('100')
        remainder('1N')
        self.assertEqual(memory_as_int(), 1)

    def test_negate(self):
        add('100')
        negate()
        self.assertEqual(memory_as_int(), -9)

    def test_store(self):
        store('100')
        self.assertEqual(memory_as_int(), 9)

    def test_bttoint(self):
        self.assertEqual(bt_to_int('1N10'), 21)

    def test_inttobt(self):
        self.assertEqual(int_to_bt(21), '1N10')

    def test_memoryasint(self):
        store('1NN0')
        self.assertEqual(memory_as_int(), 15)

    def test_memoryasbt(self):
        store('1NN0')
        self.assertEqual(memory_as_bt(), '1NN0')

    def test_evaluate(self):
        self.assertEqual(evaluate('=1NN1 + N01*1N'), "1NN1")
        self.assertEqual(evaluate('100'), "needs an operator")
        self.assertEqual(evaluate('-+10'), "operator error")
        self.assertEqual(evaluate('98'), "invalid input")
        
unittest.main()
