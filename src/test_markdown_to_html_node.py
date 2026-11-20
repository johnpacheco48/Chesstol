import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_html_node import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_md_to_html_node(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )

    def test_md_to_html_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>"
        )

    def test_md_to_html_quoteblock(self):
        md = """>This is text that _should_ remain
>the **same** even with inline stuff"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that <i>should</i> remain\nthe <b>same</b> even with inline stuff</blockquote></div>"
        )

    def test_md_to_html_ul(self):
        md = """- This is text that _should_ remain
- the **same** even with inline stuff"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is text that <i>should</i> remain</li><li>the <b>same</b> even with inline stuff</li></ul></div>"
        )

    def test_md_to_html_ol(self):
        md = """1. This is text that _should_ remain
2. the **same** even with inline stuff"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is text that <i>should</i> remain</li><li>the <b>same</b> even with inline stuff</li></ol></div>"
        )

    def test_md_to_html_h(self):
        md = """#### This is text that _should_ remain"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><h4>This is text that <i>should</i> remain</h4></div>"""
        )

if __name__ == "__main__":
    unittest.main()
