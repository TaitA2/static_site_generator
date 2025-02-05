from textnode import TextNode
from htmlnode import *
from node_splitters import *
from blocks import *
import re

tag_dict = {"bold": "b", "italic": "i", "code": "code", "link": "a", "img": "img", "list_item": "li",   # inline tags
            "paragraph": "p", "heading": "h", "code": "code", "quote": "blockquote", "unordered_list": "ul", "ordered_list": "ol" }  # block tags

# convert raw string to list of TextNodes
def text_to_textnodes(text):
    text_node = TextNode(text, "text",)
    img_split = split_nodes_image([text_node])
    link_split = split_nodes_link(img_split)
    code_split = split_nodes_delimiter(link_split, "`", "code")
    bold_split = split_nodes_delimiter(code_split, "**", "bold")
    italic_split = split_nodes_delimiter(bold_split, "*", "italic")
    alt_italic_split = split_nodes_delimiter(italic_split, "_", "italic")
    
    return alt_italic_split

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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    # print(blocks)
    block_nodes = []
    for block in blocks:
        # find block type
        block_type = block_to_block_type(block)
        # find tag
        tag = tag_dict[block_type]

        # add different header tags eg h1, h2 and remove leading '#'s
        if block_type == "heading":
            hashes = "".join(re.findall(r"^#+", block))
            hash_count = len(hashes)
            tag = f"{tag}{hash_count}"
            block = block.replace(hashes, "").strip()
        
        # remove backticks from code block
        if block_type == "code":
            block = block.replace("```", "")

        if block_type == "quote":
            block = block[1:].strip()
        
        children = []
        # add <li> to list items
        if block_type == ("unordered_list"):
            list_items = re.split(r"\n *\* +", block[1:])
            list_items = [item.strip() for item in list_items if item]
            # add italics to list items
            text_nodes = [(text_to_textnodes(f"<li>{li}</li>")) for li in list_items]
            text_nodes = [item for sublist in text_nodes for item in sublist]

        elif block_type == ("ordered_list"):
            list_items = re.split(r"\d+\. ", block)
            list_items = [item.strip() for item in list_items if item]
            # add italics to list items
            text_nodes = [(text_to_textnodes(f"<li>{li}</li>")) for li in list_items]
            text_nodes = [item for sublist in text_nodes for item in sublist]

        else:
            text_nodes = text_to_textnodes(block)
        children = [text_node_to_html_node(node) for node in text_nodes]
        # print(text_nodes)
        

        
        
        # create html node
        block_node = ParentNode(tag=tag, children=children)
        block_nodes.append(block_node)
    
    html_blocks = [block.to_html() for block in block_nodes]
  
    return "<div>"+"".join(html_blocks)+"</div>"

def main():
    test_node = TextNode("bold test", "bold")
    # print(text_node_to_html_node(test_node).to_html())
    # text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # nodes = text_to_textnodes(text)
    # print(nodes)

    markdown = """
    # This is the heading.

    This is text with a **bold** word, an *italic* word, a `code block`, an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg), and a [link](https://boot.dev)

    * This is an unordered list block
    * with three list items
    * like this one
    * AND THIS RISKY *ITALIC* ONE
    * AND THE ALTERNATIVE _ITALIC_ ONE
    * but does it support a [link](https://boot.dev)

    1. This is an ORDERED list
    2. I don't think it works

    ```This is a code block```
    """
    html_node = markdown_to_html_node(markdown)
    print(html_node)
    # print(">\n<".join(html_node.split("><")))

if __name__ == "__main__":
    main()