import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "text"})
        print("HTMLNode __repr__:", repr(node))
        node2 = HTMLNode("h1", "This is a heading")
        node3 = HTMLNode("a", "this is a link", props={"href": "https://example.com"})
        node4 = LeafNode("p", "This is a leafy boy")
        print("LeafNode to html (node4):", node4.to_html())
        node5 = LeafNode("img", "Look at this sick pic", props=({"src": "image.jpg"}))
        node6 = ParentNode("h1", [node4, node5])
        print("ParentNode to html:", node6.to_html())

if __name__ == "__main__":
    unittest.main() 