import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com"})
        result = node.props_to_html()
        expected = ' href="https://google.com"'
        self.assertEqual(result, expected)

    def test_props2(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(result, expected)
        

    def test_props3(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com", "target": "_blank", "rel": "alternate"})
        result = node.props_to_html()
        expected = ' href="https://google.com" target="_blank" rel="alternate"'
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main()