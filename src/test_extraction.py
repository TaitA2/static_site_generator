import unittest

from extraction import *

class TestImageExtraction(unittest.TestCase):
    def test_img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)

    def test_no_img(self):
        text = "This text has no link or img inside"
        result = extract_markdown_images(text)
        expected = []
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
        

class TestLinkExtraction(unittest.TestCase):
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
    
    def test_no_link(self):
        text = "This text has no link or img inside"
        result = extract_markdown_links(text)
        expected = []
        # print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
        
class TestTitleExtraction(unittest.TestCase):
    def test_title(self):
        markdown = "# This is the title\n\n## This is not"
        result = extract_title(markdown)
        expected = "This is the title"
        print(f"\nExpected:\n{expected}\nActual:\n{result}")
        self.assertEqual(result, expected)
        
    def test_exception(self):
        with self.assertRaises(Exception, msg="no h1 element found for title extraction"):
            markdown = "## There is no title here"
            result = extract_title(markdown)
            

if __name__ == "__main__":
    unittest.main()