import unittest
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


class Testdelimiter(unittest.TestCase):
    def test_md_to_blocks(self):
        text ="""
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        blocks = markdown_to_blocks(text)
        eq = ["""# This is a heading""", "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", "- This is the first list item in a list block\n- This is a list item\n- This is another list item"]
        self.assertEqual(blocks, eq)
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_to_block_par(self):
        block = "This is a string of text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    def test_block_to_block_head(self):
        block = """# This is a string of text"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_block_to_block_code(self):
        block = """```
This is a string of text
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    def test_block_to_block_quote(self):
        block = """>This is a string of text"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

if __name__ == "__main__":
    unittest.main()
