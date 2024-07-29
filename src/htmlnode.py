class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag      # html tag eg p, a, h1 etc.
        self.value = value  # text inside tag
        self.children = children    # list of HTMLNode object children of this node
        self.props = props  # dict of attribute type: attribute e.g {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # returns prop dict formatted as KEY="VALUE" eg "target": "_blank" becomes target="_blank"
        d = self.props
        if d:
            d_list = [f' {key}="{value}"' for key, value in d.items()]
            return "".join(d_list)
        return ""

    def __repr__(self):
        # return string representation of HTMLNode object
        return f"{type(self).__name__}(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


# LeafNode child class of HTMLNode 
class LeafNode(HTMLNode):

    # similar to parent but no children and value is required
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
        

    def to_html(self):
        
        # raise ValueError if missing value
        if self.value == None:
            raise ValueError("no value argument found")
        
        # return value as raw text if no tag
        if not self.tag:
            return self.value

        # convert to html
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):

    # similar to parent but no value and children is required
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        # raise value error if no tag or children
        if not self.tag:
            raise ValueError("no tag argument found")
        if not self.children:
            raise ValueError("no children argument found")
        
        # TODO return string for html tag of node and its children
        html_list = []
        for node in self.children:
            if type(node).__name__ != LeafNode:
                node.to_html()

            html_list.append(node.to_html())
        html_string = "".join(html_list)
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"


def main():
    test_html = HTMLNode("a", "Click me!", [], {"href": "https://www.google.com"})
    test_leaf =  LeafNode("p", "This is a paragraph of text.")
    test_parent = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode("p", [LeafNode(None, "Nested text")])
    ], {"href": "test.com"}
)
    # print(test_html)
    # print(test_leaf)
    print(test_parent.to_html())
    
main()