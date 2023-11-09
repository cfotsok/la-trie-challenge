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

        """Pour chaque lettre du mot à la position n: 
        La lettre fait partie des clés du dictionnaire à la prodondeur n ?
            Non: 
                On l'ajoute avec son booléen pour signaler s'il s'agit de la fin du mot ou pas.
            Oui:
                La lettre est la dernière du mot ?
                 Oui: on signale que c'est la fin du mot.
        On récupère le nœuds suivant de la trie
        """
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
