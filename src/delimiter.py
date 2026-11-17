import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    final = []
    for old_node in old_nodes:
        new_nodes = []
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        elif delimiter in old_node.text:
            split_text = old_node.text.split(delimiter, maxsplit = 1)
            if delimiter not in split_text[1]: raise Exception("Found no closing delimiter")
            else:
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                split_text2 = split_text[1].split(delimiter, maxsplit = 1)
                new_nodes.append(TextNode(split_text2[0], text_type))
                if split_text2[1] != "":
                    new_nodes.append(TextNode(split_text2[1], TextType.TEXT))


        else: raise Exception(f"Delimiter {delimiter} was not found in text")

        final.append(new_nodes)

    return final

def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
#print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
