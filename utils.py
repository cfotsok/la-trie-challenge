import json
from dataclasses import dataclass


@dataclass
class Trie:
    content: dict = None
    word: str = ""

    def add(self, word: str):
        # Initialisation du dict pour le premier élément
        if not self.content:
            self.content = {}

        # Formattage
        word = word.lower().strip()
        node = self.content

        """Pour chaque lettre du mot à la position n: 
        La lettre fait partie des clés du dictionnaire à la prodondeur n ?
            Non: 
                On l'ajoute avec son booléen pour signaler s'il s'agit de la fin du mot ou pas.
            Oui:
                La lettre est la dernière du mot ?
                 Oui: on signale que c'est la fin du mot.
        On récupère le nœuds suivant de la trie
        """
        for letter in word:
            if letter not in node.keys():
                node[letter] = {"is_word": word.endswith(letter)}
            elif word.endswith(letter):
                node["is_word"] = True
            node = node.get(letter)

        with open('trie.json', 'w') as f:
            json.dump(self.content, f, indent=4, ensure_ascii=False)

    def contains(self, word):
        if not self.content:
            return False

        word = word.lower().strip()
        node = self.content

        for letter in word:
            if letter in node.keys():
                node = node.get(letter)
                if word.endswith(word[-1]) and node.get("is_word"):
                    return True
        else:
            return False
