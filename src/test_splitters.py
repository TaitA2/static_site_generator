import unittest
from node_splitters import *
from textnode import *
class TestSplitNodes(unittest.TestCase):

    # test for code block
    def test_code_block(self):
        old_node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([old_node], "`", "code")
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),]
        print(f"\nExpected:\n{expected}\nActual:\n{new_nodes}")
        self.assertEqual(new_nodes, expected)

    # test for italic
    def test_italic(self):
        old_node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([old_node], "*", "italic")
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text"),]
        print(f"\nExpected:\n{expected}\nActual:\n{new_nodes}")
        self.assertEqual(new_nodes, expected)

    # test for bold 
    def test_bold(self):
        old_node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([old_node], "**", "bold")
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word", "text"),]
        print(f"\nExpected:\n{expected}\nActual:\n{new_nodes}")
        self.assertEqual(new_nodes, expected)

    # test for no closing delimiter
    def test_loose_end(self):
        with self.assertRaises(Exception, msg="closing delimiter not found"):
            old_node = TextNode("This is text with a **bold word", "text")
            split_nodes_delimiter([old_node], "**", "bold")

if __name__ == "__main__":
    unittest.main()