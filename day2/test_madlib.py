import unittest


def prompt_str(type):
    return f"{type.ljust(10)}: "


class TestMadlib(unittest.TestCase):
    def test_prompt_str(self):
        self.assertEqual(prompt_str("Noun"), "Noun      : ")
        self.assertEqual(prompt_str("Location"), "Location  : ")
        self.assertEqual(prompt_str("Verb"), "Verb      : ")


if __name__ == "__main__":
    unittest.main()
