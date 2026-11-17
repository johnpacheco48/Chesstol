import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class Testdelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a **text** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        eq = [[TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" node", TextType.TEXT)]]
        self.assertEqual(new_nodes, eq)
    def test_italic(self):
        node = TextNode("_This_ is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        eq = [[TextNode("This", TextType.ITALIC, None), TextNode(" is a text node", TextType.TEXT, None)]]
        self.assertEqual(new_nodes, eq)
    def test_code(self):
        node = TextNode("This `is a text node`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        eq = [[TextNode("This ", TextType.TEXT), TextNode("is a text node", TextType.CODE)]]
        self.assertEqual(new_nodes, eq)
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)



if __name__ == "__main__":
    unittest.main()
