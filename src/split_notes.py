from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
          raise Exception("Input must be a TextNode")

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
                
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' found in: {node.text}")
        
        split_nodes = node.text.split(delimiter)
        for index, chunk in enumerate(split_nodes):
            if index % 2 == 0:
                new_nodes.append(TextNode(chunk, TextType.TEXT))
            else:
                new_nodes.append(TextNode(chunk, text_type))
            
    return new_nodes
    

        
        
        
 
            
    
        
            
    
