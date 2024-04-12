# You can (and should) organize tests into multiple
# classes so that related tests go together.
#
# You can target tests by class or name.
#
#   python main-6.py
#   python main-6.py -v
#   python main-6.py -v TestIntegerMethods
#   python main-6.py -v TestIntegerMethods.test_addition
#
# NOTE -v is a flag that changes how the program runs. You
# often can (and should) try -h or --help because programs
# typically tell you what they can do.
#
# READ THE * MANUAL

import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())


class TestIntegerMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)


if __name__ == "__main__":
    unittest.main()
