# convert raw markdown to list of "block" strings

def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        block.strip()
        if block == "":
            blocks.remove(block)
    return blocks




def main():
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    blocks = markdown_to_block(markdown)
    for b in blocks:
        print(f"\nblock:\n{b}")

if __name__ == "__main__":
    main()

