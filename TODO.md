# TODO

### make markdown_to_html_node(markdown) function

1. Split the markdown into blocks (you already have a function for this)
2. Loop over each block:
    - Determine the type of block (you already have a function for this)
    - Based on the type of block, create a new HTMLNode with the proper data
    - Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
3. Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
