from enum import Enum



class BlockType(Enum):
    PARAGRAPH = None
    HEADING = """#"""
    CODE = "`"
    QUOTE = ">"
    UNORDERED_LIST = "-"
    ORDERED_LIST = "1."

def block_to_block_type(block) -> BlockType:
    match 1:
        case 1 if block.startswith("""#"""):
            return BlockType.HEADING
        case 1 if block.startswith("```\n"):
            return BlockType.CODE
        case 1 if block.startswith(">"):
            return BlockType.QUOTE
        case 1 if block.startswith("- "):
            return BlockType.UNORDERED_LIST
        case 1 if block.startswith("1. "):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    split = markdown.split("\n\n")
    for text in split:
        if text != "":
            blocks.append(text.strip())
    return blocks
