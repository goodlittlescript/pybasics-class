import unittest


class TestIntegerMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(1 + -2, -1)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)
        self.assertEqual(2 - -1, 3)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_exponentiation(self):
        self.assertEqual(2**0, 1)
        self.assertEqual(2**1, 2)
        self.assertEqual(2**2, 4)
        self.assertEqual(2**3, 8)
        self.assertEqual(2**4, 16)
        self.assertEqual(2**5, 32)
        self.assertEqual(2**6, 64)
        self.assertEqual(2**7, 128)
        self.assertEqual(2**8, 256)

    def test_division(self):
        self.assertEqual(4 / 2, 2)
        # What is this?? Try changing the expected value or places.
        self.assertAlmostEqual(4 / 3, 1.33, places=2)

    def test_floor_division(self):
        self.assertEqual(4 // 2, 2)
        # How is this different than regular division?
        self.assertEqual(4 // 3, 1)

    def test_modulus(self):
        # Any guesses what this is? Prove it with more assertions...
        self.assertEqual(10 % 1, 0)
        self.assertEqual(10 % 2, 0)
        self.assertEqual(10 % 3, 1)
        self.assertEqual(10 % 4, 2)
        self.assertEqual(10 % 5, 0)
        self.assertEqual(10 % 6, 4)
        self.assertEqual(10 % 7, 3)
        self.assertEqual(10 % 8, 2)
        self.assertEqual(10 % 9, 1)
        self.assertEqual(10 % 10, 0)

    def test_order_of_operations(self):
        # use parens to disambiguate order of operations
        self.assertEqual(1 + 2, 3)
        self.assertEqual(1 + 2 * 3, 7)
        self.assertEqual((1 + 2) * 3, 9)

        # stuff like this is super technical and therefore
        # error-prone... we'll see later how tests help
        # refactor (aka "rewrite with the same result")
        # difficult code into easier code
        self.assertEqual(10 - ((7 // 2) * 3) + 1, 2)


if __name__ == "__main__":
    unittest.main()
