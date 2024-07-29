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
        d_list = [f' {key}="{value}"' for key, value in d.items()]
        return "".join(d_list)

    def __repr__(self):
        # return string representation of HTMLNode object
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

def main():
    test = HTMLNode("h1", "header", [], {"href": "https://google.com"})
    print(test)

main()