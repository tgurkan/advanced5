import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_subtract2(self):
		result = rpn.calculate("3 5 -")
		self.assertEqual(-2, result)
	def test_multiply(self):
		result = rpn.calculate("1 2 *")
		self.assertEqual(2, result)
	def test_multiply2(self):
		result = rpn.calculate("0 2 *")
		self.assertEqual(0, result)
	def test_multiply2(self):
		result = rpn.calculate("0 0 *")
		self.assertEqual(0, result)
	def test_divide(self):
		result = rpn.calculate("4 2 /")
		self.assertEqual(2, result)
	def test_badstring(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 5 3 -")
	def test_badstring2(self):
		with self.assertRaises(TypeError):
			rpn.calculate("A 5 3 -")