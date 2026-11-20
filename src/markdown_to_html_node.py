from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes, TextType
from textnode import TextNode, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                text = block.replace("\n", " ")
                html_nodes.append(ParentNode("p", get_leaf_nodes(text)))
            case BlockType.HEADING:
                text = block.split(" ", 1)[1]
                html_nodes.append(ParentNode(f"h{get_heading(block)}", get_leaf_nodes(text)))
            case BlockType.CODE:
                text = block.replace("```", "").strip()
                leaf_node = text_node_to_html_node(TextNode(text, TextType.TEXT))
                parent_1 = ParentNode("code", [leaf_node])
                html_nodes.append(ParentNode("pre", [parent_1]))
            case BlockType.QUOTE:
                text = block.replace(">", "").strip()
                html_nodes.append(ParentNode("blockquote", get_leaf_nodes(text)))
            case BlockType.UNORDERED_LIST:
                child_nodes = []
                for line in block.split("-"):
                    if line == "": pass
                    else: child_nodes.append(ParentNode("li", get_leaf_nodes(line.strip())))
                text = block.replace("-", "").strip()
                html_nodes.append(ParentNode("ul", child_nodes))
            case BlockType.ORDERED_LIST:
                child_nodes = []
                for line in block.split("\n"):
                    if line == "": pass
                    else: child_nodes.append(ParentNode("li", get_leaf_nodes(line.split(".")[1].strip())))
                html_nodes.append(ParentNode("ol", child_nodes))

    big_mommy_node = ParentNode("div", html_nodes)
    return big_mommy_node

def get_leaf_nodes(block: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def get_heading(block: str) -> int:
    return sum(1 for _ in block.split(" ", 1)[0])
