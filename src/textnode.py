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
        return f"TextNode({self.text}, {self.text_type}, {self.url})" if self.url != None else f"TextNode({self.text}, {self.text_type})"


def main():
    test = TextNode("this is a test", "link", "https://www.google.com" )
    print(test)

if __name__ == "__main__":
    main()