import unittest
from node_splitters import *
from textnode import *
class TestSplitDelimiter(unittest.TestCase):

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

class TestSplitImage(unittest.TestCase):
    def test_img(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text",)
        new_nodes = split_nodes_image([node])
        expected = [TextNode("This is text with a ", "text"), 
                    TextNode("rick roll", "img", "https://i.imgur.com/aKaOqIh.gif"), 
                    TextNode(" and ", "text"), 
                    TextNode("obi wan", "img", "https://i.imgur.com/fJRm4Vk.jpeg")]
        print(f"\nExpected:\n{expected}\nActual:\n{new_nodes}")
        self.assertEqual(new_nodes, expected)

class TestSplitLink(unittest.TestCase):
    def test_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",)
        new_nodes = split_nodes_link([node])
        expected = [TextNode("This is text with a link ", "text"),
                    TextNode("to boot dev", "link", "https://www.boot.dev"),
                    TextNode(" and ", "text"),
                    TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),]
        print(f"\nExpected:\n{expected}\nActual:\n{new_nodes}")
        self.assertEqual(new_nodes, expected)



if __name__ == "__main__":
    unittest.main()