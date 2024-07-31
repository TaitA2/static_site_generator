import unittest
from blocks import *

class TestMdToBlock(unittest.TestCase):
    def test_heading(self):
        markdown = "# This is a heading"
        result = markdown_to_block(markdown)
        expected = ["# This is a heading"]
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_code(self):
        markdown = ""
        result = markdown_to_block(markdown)
        expected = ""
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_quote(self):
        markdown = ""
        result = markdown_to_block(markdown)
        expected = ""
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = ""
        result = markdown_to_block(markdown)
        expected = ""
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        markdown = ""
        result = markdown_to_block(markdown)
        expected = ""
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        pass

    def test_code(self):
        pass

    def test_quote(self):
        pass

    def test_unordered_list(self):
        pass

    def test_ordered_list(self):
        pass