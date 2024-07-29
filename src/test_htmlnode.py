import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

# test html nodes
class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com"})
        result = node.props_to_html()
        expected = ' href="https://google.com"'
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_props2(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = ' href="https://google.com" target="_blank"'
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
        

    def test_props3(self):
        node = HTMLNode("a", "link", [], {"href": "https://google.com", "target": "_blank", "rel": "alternate"})
        result = node.props_to_html()
        expected = ' href="https://google.com" target="_blank" rel="alternate"'
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

# test leaf nodes
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

# test parent nodes
class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

        result = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
    
    def test_nested(self):
        node = ParentNode(
            "body",
            [ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )]
        )
        result = node.to_html()
        expected = "<body><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_childless(self):
        with self.assertRaises(ValueError, msg="no children argument found"):
            node = ParentNode(
                "p",
                []
            )
            result = node.to_html()
    

if __name__ == "__main__":
    unittest.main()