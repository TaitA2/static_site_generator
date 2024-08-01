# extract alt text / url from img or link from raw markdown text

# import regular expresssion library
import re
# extract alt text and href 
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def extract_title(markdown):
    title = "".join(re.findall(r"^#(?!#).*\n", markdown))[1:].strip()
    if title:
        return title
    else:
        raise Exception("no h1 element found for title extraction")

def main():
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
    # # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    # text = "This text has no link or img inside"
    # print(extract_markdown_images(text))

    # extract title
    markdown = "# this is the title\n\n##This is not"
    print(extract_title(markdown))
if __name__ == "__main__":
    main()
