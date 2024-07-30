class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        # return True if all properties same between 2 TextNode objects
        return True if (self.text, self.text_type, self.url) == (target.text, target.text_type, target.url) else False
    
    def __repr__(self):
        # return string representation of TextNode object
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

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

def main():
    # test = TextNode("this is a test", "link", "https://www.google.com" )
    # print(test)
    node = TextNode("This is text with a **bold** word", "text")
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    for n in new_nodes:
        print(n)

if __name__ == "__main__":
    main()