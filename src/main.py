from textnode import *

def main():
    node = TextNode("This is a text node", TextType.BOLD_TEXT, "http://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()