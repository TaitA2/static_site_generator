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

# convert one text node into list of text nodes based on links
def split_node_link(old_nodes):
    # list of new nodes to be returned
    new_nodes = []


def main():
    pass

if __name__ == "__main__":
    main()