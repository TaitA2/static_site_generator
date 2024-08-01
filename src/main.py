import os
import shutil
from node_conversion import *

# recursively copy contents of source dir to destination dir
def recursive_copy(source, dest):
    # make destination dir if none exists
    if not os.path.exists(dest):
        os.mkdir(dest)
    # iterate over contents of source dir
    for file in os.listdir(source):
        # set paths to be source/file and dest/file
        from_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)
        # print paths for insight and debugging
        print(f"* {from_path} -> {dest_path}")
        # copy files across and call this func on dirs
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_copy(from_path, dest_path)

# generate webpage from markdown
def generate_page(from_path, template_path, dest_path):

    # insightful print message
    print(f"\n* Generating page from {from_path} to {dest_path} using {template_path}...\n\n")
    # read markdown file at from_path and assign to var
    from_file = open(from_path).read()
    # read template file at template_path and assign to var
    template_file = open(template_path).read()
    # convert markdown file to html string
    content = markdown_to_html_node(from_file)
    # print(">\n<".join(html_string.split("><")))
    # find title of webpage from markdown
    title = extract_title(from_file)
    # print(title)
    # replace template title and content with actual title and content
    index_file = template_file.replace("{{ Title }}", title).replace("{{ Content }}", content)
    # print(template_file)
    # wrtie index_file to dest_path/index.html
    open(dest_path, "w").write(index_file)
    print("Done!!")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(from_path):
            # Ensure the corresponding directory exists in dest_dir_path
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            # Recursively call the function for subdirectories
            generate_pages_recursive(from_path, template_path, dest_path)
        elif entry.endswith(".md"):
            # Change the destination file name to end with .html
            dest_file_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(from_path, template_path, dest_file_path)

# Main function to run the operations
def main():
    # Delete all files in public/ and copy files from static/ to public/
    recursive_copy("static/", "public/")
    # Generate pages from the content directory
    generate_pages_recursive("content/", "template.html", "public/")

if __name__ == "__main__":
    main()