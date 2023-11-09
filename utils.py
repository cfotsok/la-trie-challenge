import json
from dataclasses import dataclass


@dataclass
class Trie:
    content: dict = None

    def add(self, word: str):
        # Initialisation du dict pour le premier élément
        if not self.content:
            self.content = {}

        # Formattage
        word = word.lower().strip()
        letters = list(word)
        node = self.content

        for letter in letters:
            if letter not in node.keys():
                node[letter] = {"is_word": word.endswith(letter)}
            elif word.endswith(letter):
                node["is_word"] = True
            node = node.get(letter)

        with open('trie.json', 'w') as f:
            json.dump(self.content, f, indent=4, ensure_ascii=False)

    def contains(self, word):
        pass
