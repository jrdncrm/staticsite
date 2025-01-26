from textnode import *


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{(" " + self.props_to_html()) if self.props else ""}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        else:
            children_html = ''.join(node.to_html() for node in self.children)
            return f'<{self.tag}{(" " + self.props_to_html()) if self.props else ""}>{children_html}</{self.tag}>'

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode): 
        raise Exception("Input must be a TextNode")
    match(text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, {text_node.text})
        case (TextType.BOLD):
            return LeafNode("b", {text_node.text})
        case (TextType.ITALIC):
            return ("i", {text_node.text})
        case (TextType.CODE):
            return ("code", {text_node.text})
        case (TextType.LINK):
            return ("a", {text_node.text}, {"href": text_node.url})
        case (TextType.IMAGE):  
            return ("img", {text_node.text}, {"src":text_node.url})