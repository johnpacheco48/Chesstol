import code
from posix import link
import re

from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if len(old_node.text.split(delimiter)) == 1:
            new_nodes.append(old_node)
            continue

        elif delimiter in old_node.text:
            split_text = old_node.text.split(delimiter)
            if len(split_text) % 2 == 0: raise Exception("Found no closing delimiter")
            else:
                for text in split_text:
                    if split_text.index(text) % 2 == 0:
                        if text == "": pass
                        else: new_nodes.append(TextNode(text, TextType.TEXT))
                    else:
                        if text == "": pass
                        else: new_nodes.append(TextNode(text, text_type))

    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if matches == None or "": raise Exception("Unable to extract image link or alt-text")
    return matches
#print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if matches == None or "": raise Exception("Unable to extract link")
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        alt_link_list = extract_markdown_images(old_node.text)
        if alt_link_list == "":
            new_nodes.append(old_node)
            continue
        remaining = old_node.text
        for alt_link in alt_link_list:
            first_split = remaining.split(f"![{alt_link[0]}]({alt_link[1]})", 1)
            if first_split[0] != "":
                new_nodes.append(TextNode(first_split[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_link[0], TextType.IMAGE, alt_link[1]))
            remaining = first_split[1]
        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))


    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        alt_link_list = extract_markdown_links(old_node.text)
        if alt_link_list == "":
            new_nodes.append(old_node)
            continue

        remaining = old_node.text
        for alt_link in alt_link_list:
            first_split = remaining.split(f"[{alt_link[0]}]({alt_link[1]})", 1)
            if first_split[0] != "":
                new_nodes.append(TextNode(first_split[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_link[0], TextType.LINK, alt_link[1]))
            remaining = first_split[1]
        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))


    return new_nodes
