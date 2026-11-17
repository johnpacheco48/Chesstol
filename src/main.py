from textnode import TextNode, TextType


def main():
    dummy = TextNode()
    dummy.text = "Chesstol: Learn chess faster than a Pistol!"
    dummy.text_type = "BOLD"
    dummy.url = "https://www.chesstol.com"
    print(dummy)
    return dummy
main()
