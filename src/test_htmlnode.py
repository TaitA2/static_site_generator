import unittest

from htmlnode import HTMLNode, LeafNode

# test html nodes
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

# test leaf nodes
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected)
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)

    

if __name__ == "__main__":
    unittest.main()