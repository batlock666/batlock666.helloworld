# NOQA: D100

import unittest

from batlock666.helloworld import hello_world


class HelloWorldTestCase(unittest.TestCase):  # NOQA: D101

    def test_hello_world_without_name(self):  # NOQA: D102
        self.assertEqual(hello_world(), "Hello, World!")

    def test_hello_world_with_name(self):  # NOQA: D102
        self.assertEqual(hello_world("John"), "Hello, John!")


if __name__ == "__main__":
    unittest.main()
