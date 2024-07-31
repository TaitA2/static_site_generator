from textnode import TextNode
from htmlnode import *
from node_splitters import *
from blocks import *

tag_dict = {"bold": "b", "italic": "i", "code": "code", "link": "a", "img": "img",   # inline tags
            "paragraph": "p", "heading": "h", "code": "code", "quote": "blockquote", "unordered_list": "ul", "ordered_list": "ol" }  # block tags

# convert text node to html node
def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    # text type text
    if text_type == "text":
        return LeafNode(None,text)   

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

# convert raw string to list of TextNodes
def text_to_textnodes(text):
    text_node = TextNode(text, "text",)
    img_split = split_nodes_image([text_node])
    link_split = split_nodes_link(img_split)
    code_split = split_nodes_delimiter(link_split, "`", "code")
    bold_split = split_nodes_delimiter(code_split, "**", "bold")
    italic_split = split_nodes_delimiter(bold_split, "*", "italic")
    
    return italic_split


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        # find block type
        block_type = block_to_block_type(block)
        # find tag
        tag = tag_dict[block_type]


        # create list of inline HTMLNodes
        # avoids error with list items and italic sharing a prefix
        if tag == "ul":
            text_nodes = text_to_textnodes(block[1:])
        else:
            text_nodes = text_to_textnodes(block)

        children = [text_node_to_html_node(node) for node in text_nodes]

        # create html node
        block_node = ParentNode(tag=tag, children=children)
        block_nodes.append(block_node)
    
    html_blocks = [block.to_html() for block in block_nodes]
  
    return "<div>"+"".join(html_blocks)+"</div>"


test_node = TextNode("bold test", "bold")
# print(text_node_to_html_node(test_node).to_html())
# text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# nodes = text_to_textnodes(text)
# print(nodes)

markdown = "# This is the heading.\nThis is a **bold** word, an *italic* word in a paragraph"
print(markdown_to_html_node(markdown))