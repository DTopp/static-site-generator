from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, World!", TextType.NORMAL)
    print(node)
    link_node = TextNode("OpenAI", TextType.LINK, "https://www.openai.com")
    print(link_node)

if __name__ == "__main__":
    main()