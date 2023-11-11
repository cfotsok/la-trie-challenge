from dataclasses import dataclass


class Node:
    def __init__(self, value):
        self.value: str = value
        self.children: dict[str, Node] = {}
        self.parent: (str, Node) = ()
        self.is_word: bool = False
        self.visited: list = []


@dataclass
class Trie(object):
    root: Node = Node("")
    word = ""
    i = 0
    indent = 0

    def add(self, word: str):
        node = self.root
        word = word.lower().strip()
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
                new_node.parent = (node.value, node)
                node = new_node
        node.is_word = True

    def contains(self, word):
        node = self.root
        word = word.lower().strip()
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return node.is_word

    def affiche(self, node=root, prefix=""):
        if node.is_word:
            self.word = prefix
            print(f"⏐")
            self.word = ""

        for child in node.children.values():
            if self.i > 0:
                print(f"⏐", end="")

            print("   " * self.i + f"⏐⎯ {child.value} ", end="")
            end = f"*[{prefix + child.value}]" if child.is_word else ""
            print(end)

            self.i += 1
            self.affiche(child, prefix + child.value)

            self.i -= 1


