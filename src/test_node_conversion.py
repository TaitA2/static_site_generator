import unittest

from textnode import *
from htmlnode import *
from node_conversion import *

# test conversion of TextNodes to HTMLNodes
class TestTextNodeToHTHMLNode(unittest.TestCase):

    # test bold text type
    def test_bold(self):
        text_node = TextNode("bold test", "bold")
        html_node = text_node_to_html_node(text_node)
        expected = "<b>bold test</b>"
        result = html_node.to_html()
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test italic text type
    def test_italic(self):
        text_node = TextNode("italic test", "italic")
        html_node = text_node_to_html_node(text_node)
        expected = "<i>italic test</i>"
        result = html_node.to_html()
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test link text type
    def test_link(self):
        text_node = TextNode("link test", "link", "https://www.link_test.com")
        html_node = text_node_to_html_node(text_node)
        expected = '<a href="https://www.link_test.com">link test</a>'
        result = html_node.to_html()
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test img text type
    def test_img(self):
        text_node = TextNode("img test", "img", "https://www.img_test.com")
        html_node = text_node_to_html_node(text_node)
        expected = '<img src="https://www.img_test.com" alt="img test"></img>'
        result = html_node.to_html()
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test invalid text type (eg underline)
    def test_invalid(self):
        with self.assertRaises(Exception, msg="Invalid text type"):
            text_node = TextNode("invalid test", "underline")
            html_node = text_node_to_html_node(text_node)
            
# test conversion of raw text to list of TextNodes
class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [TextNode("This is ", "text"), 
                    TextNode("text", "bold"), 
                    TextNode(" with an ", "text"), 
                    TextNode("italic", "italic"), 
                    TextNode(" word and a ", "text"), 
                    TextNode("code block", "code"), 
                    TextNode(" and an ", "text"), 
                    TextNode("obi wan image", "img", "https://i.imgur.com/fJRm4Vk.jpeg"), 
                    TextNode(" and a ", "text"), 
                    TextNode("link", "link", "https://boot.dev")]
        # print(f"\nExpected:\n{expected}\nActual:\n{nodes}")
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()