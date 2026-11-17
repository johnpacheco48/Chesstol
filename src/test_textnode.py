import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("text", TextType.BOLD)
        node2 = TextNode("text", TextType.BOLD, "https://www.hi.com")
        self.assertNotEqual(node, node2)
    def test_uneq_type(self):
        node = TextNode("text", TextType.TEXT)
        node2 = TextNode("text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_to_html1(self):
        node = TextNode("cat pic", TextType.IMAGE, "https://www.google.com/cat")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "cat pic")
        self.assertEqual(html_node.props, "https://www.google.com/cat")

if __name__ == "__main__":
    unittest.main()
