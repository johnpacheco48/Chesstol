import unittest
from textnode import TextNode, TextType
from text_to_textnodes import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes


class Testdelimiter(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        eq = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, eq)
    def test_text_to_textnodes_bold(self):
        node = "This is a **text** node"
        new_nodes = text_to_textnodes(node)
        eq = [TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" node", TextType.TEXT)]
        self.assertEqual(new_nodes, eq)
    def test_bold(self):
        node = TextNode("This is a **text** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        eq = [TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" node", TextType.TEXT)]
        self.assertEqual(new_nodes, eq)
    def test_bold_multi(self):
        node = TextNode("This **is** a text **node**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        eq = [TextNode("This ", TextType.TEXT), TextNode("is", TextType.BOLD), TextNode(" a text ", TextType.TEXT), TextNode("node", TextType.BOLD)]
        self.assertEqual(new_nodes, eq)
    def test_italic(self):
        node = TextNode("_This_ is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        eq = [TextNode("This", TextType.ITALIC, None), TextNode(" is a text node", TextType.TEXT, None)]
        self.assertEqual(new_nodes, eq)
    def test_code(self):
        node = TextNode("This `is a text node`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        eq = [TextNode("This ", TextType.TEXT), TextNode("is a text node", TextType.CODE)]
        self.assertEqual(new_nodes, eq)
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_nodes_image(self):
        node = TextNode("text0 ![alt0](link0)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        eq = [TextNode("text0 ", TextType.TEXT), TextNode("alt0", TextType.IMAGE, "link0")]
        self.assertEqual(new_nodes, eq)
    def test_split_nodes_image_multi(self):
        node = TextNode("text0 ![alt0](link0) text1 ![alt1](link1)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        eq = [TextNode("text0 ", TextType.TEXT), TextNode("alt0", TextType.IMAGE, "link0"), TextNode(" text1 ", TextType.TEXT), TextNode("alt1", TextType.IMAGE, "link1")]
        self.assertEqual(new_nodes, eq)
    def test_split_nodes_image_no_img(self):
        node = TextNode("text0", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        eq = [TextNode("text0", TextType.TEXT)]
        self.assertEqual(new_nodes, eq)

    def test_split_nodes_link(self):
        node = TextNode("text0 [alt0](link0)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        eq = [TextNode("text0 ", TextType.TEXT), TextNode("alt0", TextType.LINK, "link0")]
        self.assertEqual(new_nodes, eq)
    def test_split_nodes_link_multi(self):
        node = TextNode("text0 [alt0](link0) text1 [alt1](link1)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        eq = [TextNode("text0 ", TextType.TEXT), TextNode("alt0", TextType.LINK, "link0"), TextNode(" text1 ", TextType.TEXT), TextNode("alt1", TextType.LINK, "link1")]
        self.assertEqual(new_nodes, eq)
    def test_split_nodes_link_no_img(self):
        node = TextNode("text0", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        eq = [TextNode("text0", TextType.TEXT)]
        self.assertEqual(new_nodes, eq)

if __name__ == "__main__":
    unittest.main()
