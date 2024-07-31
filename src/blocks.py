import re
# convert raw markdown to list of "block" strings

def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            cleaned_blocks.append(block)  
    return cleaned_blocks

# return string for block type of block entered
def block_to_block_type(block):
    # default block type if no prefix found
    block_type = "paragraph"

    # regex for heading
    if re.findall(r"^#{1,6} .+", block):
        return "heading"

    # regex for code
    elif re.findall(r"^```{3}\n[\s\S]+?\n```{3}$", block):
        return "code"

    # regex for quote
    elif re.findall(r"^(> .*\n?)+", block):
        return "quote"

    # regex for ul
    elif re.findall(r"^(\* .*\n?|- .*\n?)+", block):
        return "unordered_list"

    # regex for ol
    elif re.findall(r"^(\d+\. .*\n?)+", block):
        return "ordered_list"

    # return block type
    return "paragraph"
    

			


def main():
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    blocks = markdown_to_block(markdown)
    for b in blocks:
        print(f"\nblock:\n{b}")
        print("block type:", block_to_block_type(b))

if __name__ == "__main__":
    main()

