# THIS IS A TEST FOR GIT


from textnode import *
from extraction import *

# convert one text node into list of text nodes based on delimiter e.g ' = code or ** = bold 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # list of new nodes to be returned
    new_nodes = []
    # iterate over every item in old_nodes list
    for old_node in old_nodes:
        # add the unchanged node if it is not text_type text
        if old_node.text_type != "text":
            new_nodes.append(old_node)
        # split the old node around the delimiter
        else:
            split_node = old_node.text.split(delimiter)
            # raise exception if no closing delimiter found
            if len(split_node) % 2 == 0:
                raise Exception("closing delimiter not found")
            # make new nodes of old node
            for i in range(len(split_node)):
                if i != 1:
                    new_nodes.append(TextNode(split_node[i], "text"))
                else:
                    new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes

# convert one text node into list of text nodes based on images
def split_nodes_image(old_nodes):

    # list of new nodes to be returned
    new_nodes = []
    # iterate over list of old nodes
    for old_node in old_nodes:
        text_copy = old_node.text
        # temp list
        sub_nodes = []
        # extract links etc from old node
        extracted = extract_markdown_images(text_copy)

        # return original TextNode if no img found
        if extracted == []:
            new_nodes.append(old_node)
            continue

        # replace extracted segments with '__REPLACED__'
        for e in extracted:
            img_alt = e[0]
            img_link = e[1]
            text_copy = text_copy.replace(f"![{img_alt}]({img_link})", "__REPLACED__")
        
        # split the node into segments
        split_node = text_copy.split("__REPLACED__")
        
        # convert both segments into TextNodes and add to temp list
        for segment in split_node:
            if segment != "":
                sub_nodes.append(TextNode(segment, "text"))
        
        # convert extracted img to an img TextNode and insert it in between segments in temp list
        # print(sub_nodes)
        for i in range(len(extracted)):
            try:
                node_index = 1+i+i
                new_node = (TextNode(extracted[i][0], "img", extracted[i][1]))
                sub_nodes.insert(node_index, new_node)
            except IndexError:
                pass

        # add all nodes to new_nodes list
        # print(sub_nodes)
        for sub_node in sub_nodes:
            # print(sub_node)
            new_nodes.append(sub_node) 

    return new_nodes


# convert one text node into list of text nodes based on links
def split_nodes_link(old_nodes):
    
    # list of new nodes to be returned
    new_nodes = []
    # iterate over list of old nodes
    for old_node in old_nodes:
        text_copy = old_node.text
        # temp list
        sub_nodes = []
        # extract links etc from old node
        extracted = extract_markdown_links(text_copy)

        # return original TextNode if no link found
        if extracted == []:
            new_nodes.append(old_node)
            continue

        # replace extracted segments with '__REPLACED__'
        for e in extracted:
            alt_text = e[0]
            url = e[1]
            text_copy = text_copy.replace(f"[{alt_text}]({url})", "__REPLACED__")
        
        # split the node into segments
        split_node = text_copy.split("__REPLACED__")
        
        # convert both segments into TextNodes and add to temp list
        for segment in split_node:
            if segment != "":
                sub_nodes.append(TextNode(segment, "text"))
        
        # convert extracted link to a link TextNode and insert it in between segments in temp list
        # print(sub_nodes)
        for i in range(len(extracted)):
            try:
                node_index = 1+i+i
                new_node = (TextNode(extracted[i][0], "link", extracted[i][1]))
                sub_nodes.insert(node_index, new_node)
            except IndexError:
                pass

        # add all nodes to new_nodes list
        # print(sub_nodes)
        for sub_node in sub_nodes:
            # print(sub_node)
            new_nodes.append(sub_node) 

    return new_nodes


def main():
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",
)
    new_nodes = split_nodes_image([node])
    print(node)
    print(new_nodes)
    # [
#     TextNode("This is text with a link ", text_type_text),
#     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),]

if __name__ == "__main__":
    main()