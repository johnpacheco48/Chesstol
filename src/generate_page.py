import os
import shutil

from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html_node import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path, basepath) -> None:

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = ""
    with open(from_path, mode="r") as file:
        from_file = file.read()
    template_file = ""
    with open(template_path, mode="r") as file:
        template_file = file.read()
    from_html_file = markdown_to_html_node(from_file).to_html()
    from_html_title = extract_title(from_file)

    replace_title = template_file.replace("{{ Title }}", from_html_title)
    full_html_page = replace_title.replace("{{ Content }}", from_html_file)
    href = full_html_page.replace('href="/', f'href="{basepath}')
    html_page = href.replace('src="/', f'src="{basepath}')
    with open(dest_path, mode="w") as file:
        file.write(html_page)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath) -> None:
    source_path = os.path.abspath(dir_path_content)
    dest_path = os.path.abspath(dest_dir_path)
    for dir in os.listdir(source_path):
        dir_path = os.path.join(source_path, dir)
        new_dest_path = os.path.join(dest_path, dir)
        if os.path.isfile(dir_path) and dir.split(".")[1] == "md":
            html_filename = f"{dir.split(".")[0]}.html"
            dest_file = os.path.join(dest_path, html_filename)
            generate_page(dir_path, template_path, dest_file, basepath)
            print(f"Successfully HTMLized {dir} to {dest_file}")
        if os.path.isdir(dir_path):
            os.makedirs(new_dest_path, exist_ok=True)
            #print(f"Extracting files from {dir_path}")
            generate_pages_recursive(dir_path, template_path, new_dest_path, basepath)
