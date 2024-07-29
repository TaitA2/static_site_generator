from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

# convert text node to html node
def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    # text type text
    if text_type == "text":
        html_node = LeafNode(value=text)

    # text type bold
    elif text_type == "bold":
        html_node = LeafNode("b", text)

    # text type italic
    elif text_type == "italic":
        html_node = LeafNode("i", text)

    # text type code
    elif text_type == "code":
        html_node = LeafNode("code", text)

    # text type link
    elif text_type == "link":
        html_node = LeafNode("a", text, {"href": url})

    # text type img
    elif text_type == "img":
        html_node = LeafNode("img", "", {"src": url, "alt": text})

    # raise exception if text type is none of the above
    else:
        print(text_type)
        raise Exception("Invalid text type")

    return html_node

test_node = TextNode("bold test", "bold")
print(text_node_to_html_node(test_node).to_html())