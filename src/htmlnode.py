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
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


# LeafNode child class of HTMLNode 
class LeafNode(HTMLNode):

    # similar to parent but no children and value required
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        
        # raise ValueError if missing value
        if self.value == None:
            raise ValueError
        
        # return value as raw text if no tag
        if not self.tag:
            return self.value

        # convert to html
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"



def main():
    test =  LeafNode("p", "This is a paragraph of text.")
    test2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test.to_html())
    print(test2.to_html())

main()