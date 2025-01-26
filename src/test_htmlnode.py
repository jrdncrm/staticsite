import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "text"})
        node2 = HTMLNode("h1", "This is a heading")
        node3 = HTMLNode("a", "this is a link", props={"href": "https://example.com"})
        node4 = LeafNode("p", "This is a leafy boy")
        node5 = LeafNode("img", "Look at this sick pic", props=({"src": "image.jpg"}))
        node6 = ParentNode("h1", [node4, node5])
        node7 = LeafNode("p", "This is the best paragraph")
        node8 = LeafNode("p", "No, this one is!")
        node9 = ParentNode("h2", [node7, node8])
        node10 = ParentNode("h3", [node6, node9])
        #print("ParentNode to html:", node10.to_html())

if __name__ == "__main__":
    unittest.main() 