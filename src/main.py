from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

# convert text node to html node
def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url
    tag_dict = {"bold": "b", "italic": "i", "code": "code", "link": "a", "img": "img"}

    # text type text
    if text_type == "text":
        return LeafNode(value=text)   

    # text type bold, italic, code
    elif text_type in ["bold", "italic", "code"]:
        return LeafNode(tag_dict[text_type], text)
    
    # text type link
    elif text_type == "link":
        return LeafNode("a", text, {"href": url})

    # text type img
    elif text_type == "img":
        return LeafNode("img", "", {"src": url, "alt": text})

    # raise exception if text type is none of the above
    else:
        print(text_type)
        raise Exception("Invalid text type")

    

test_node = TextNode("bold test", "bold")
print(text_node_to_html_node(test_node).to_html())