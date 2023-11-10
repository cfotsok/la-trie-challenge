from dataclasses import dataclass


class Node:
    def __init__(self, value):
        self.value: str = value
        self.children: dict[str, Node] = {}
        self.is_word: bool = False


@dataclass
class Trie:
    root: Node = Node("")

    def add(self, word: str):
        node = self.root
        word = word.lower().strip()
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
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
