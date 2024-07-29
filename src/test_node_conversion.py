import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from main import text_node_to_html_node

class TestConversion(unittest.TestCase):

    # test bold text type
    def test_bold(self):
        text_node = TextNode("bold test", "bold")
        html_node = text_node_to_html_node(text_node)
        expected = "<b>bold test</b>"
        result = html_node.to_html()
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test italic text type
    def test_italic(self):
        text_node = TextNode("italic test", "italic")
        html_node = text_node_to_html_node(text_node)
        expected = "<i>italic test</i>"
        result = html_node.to_html()
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test link text type
    def test_link(self):
        text_node = TextNode("link test", "link", "https://www.link_test.com")
        html_node = text_node_to_html_node(text_node)
        expected = '<a href="https://www.link_test.com">link test</a>'
        result = html_node.to_html()
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test img text type
    def test_img(self):
        text_node = TextNode("img test", "img", "https://www.img_test.com")
        html_node = text_node_to_html_node(text_node)
        expected = '<img src="https://www.img_test.com" alt="img test"></img>'
        result = html_node.to_html()
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(expected, result)

    # test invalid text type (eg underline)
    def test_invalid(self):
        with self.assertRaises(Exception, msg="Invalid text type"):
            text_node = TextNode("invalid test", "underline")
            html_node = text_node_to_html_node(text_node)
            

