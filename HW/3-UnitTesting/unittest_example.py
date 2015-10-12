import unittest

class TestStringMethods(unittest.TestCase):

  "Test the 'upper' method, which changes a string to upper case."
  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  "Test whether the result of an operation is True or False."
  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  "Test whether an expected exception is raised when trying to split a string on a non-string delimiter."
  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
