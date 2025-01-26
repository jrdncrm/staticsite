import unittest

from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node
from split_notes import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.ITALIC)
        node4 = TextNode("This is a different text node", TextType.ITALIC)
        node5 = TextNode("This is another node", TextType.BOLD, None)
        node6 = TextNode("This one has a url", TextType.LINK, "http://example.com")
    
        #print(text_node_to_html_node(node6)) #if image format is messed up, come back to this test case.

        unsplit1 = TextNode("This is a **test** node", TextType.TEXT)
        unsplit2 = TextNode("This is *such* a test node", TextType.TEXT)
        unsplitnodes = [unsplit1, unsplit2]

        #print(split_nodes_delimiter(unsplitnodes, "**", TextType.BOLD))
        #print(split_nodes_delimiter(unsplitnodes, "*", TextType.ITALIC)) #tests


        unsplit3 = TextNode("This is **unmatched text", TextType.TEXT)
        #print(split_nodes_delimiter([unsplit3], "**", TextType.BOLD))


        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()
