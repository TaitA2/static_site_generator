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
        markdown = "```this is a code block```"
        result = markdown_to_block(markdown)
        expected = ['```this is a code block```']
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_quote(self):
        markdown = """> This is the first line of the quote
> This is the next"""
        result = markdown_to_block(markdown)
        expected = ['> This is the first line of the quote\n> This is the next']
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = """* This is the first list item in a list block
                        * This is a list item
                        * This is another list item"""
        result = markdown_to_block(markdown)
        expected = ["""* This is the first list item in a list block
                        * This is a list item
                        * This is another list item"""]
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        markdown = """1. This is the first list item in a list block
                        2. This is a list item
                        3. This is another list item"""
        result = markdown_to_block(markdown)
        expected = ["""1. This is the first list item in a list block
                        2. This is a list item
                        3. This is another list item"""]
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_paragraph(self):
        markdown = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        result = markdown_to_block(markdown)
        expected = ["This is a paragraph of text. It has some **bold** and *italic* words inside of it."]
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        expected = "heading"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_code(self):
        block = "```this is a code block```"
        result = block_to_block_type(block)
        expected = "code"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_quote(self):
        block = '> This is the first line of the quote\n> This is the next'
        result = block_to_block_type(block)
        expected = "quote"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        block = """* This is the first list item in a list block
                        * This is a list item
                        * This is another list item"""
        result = block_to_block_type(block)
        expected = "unordered_list"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        block = """1. This is the first list item in a list block
                        2. This is a list item
                        3. This is another list item"""
        result = block_to_block_type(block)
        expected = "ordered_list"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        result = block_to_block_type(block)
        expected = "paragraph"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()