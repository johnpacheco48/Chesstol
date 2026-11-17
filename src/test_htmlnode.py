import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_3(self):
        props = {"href": "https://www.google.com"}
        html = None
        node = HTMLNode(None, None, None, props)
        self.assertNotEqual(node.props_to_html(), html)
    def test_props_to_html(self):
        props = {"target": "_blank"}
        html = ' target="_blank"'
        node = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), html)
    def test_props_to_html_2(self):
        props = {"href": "https://www.google.com"}
        html = ' href="https://www.google.com"'
        node = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), html)
    def test_leaf_to_html1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html3(self):
        node = LeafNode("img", "google", "https://www.google.com")
        self.assertEqual(node.to_html(), '<img src="https://www.google.com" alt="google" />')
    def test_parent_to_html1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html2(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b", [
                    ParentNode("c", [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),])
                ]),

            ],
        )
        self.assertEqual(node.to_html(), "<p><b><c>Normal text<i>italic text</i>Normal text</c></b></p>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
