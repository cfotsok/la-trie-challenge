from dataclasses import dataclass


class Node:
    def __init__(self, value="", is_end:bool=False):
        self.value: str = value
        self.children: dict[str, Node] = {}
        self.is_end: bool = is_end


@dataclass
class Trie(object):
    root: Node = Node()
    
    def add(self, word: str) -> None:
        def radd(node=self.root, word:str=word):
            if not word: return None
            node.children[word[0]] = Node(value=word[0].lower(), is_end=len(word) == 1)
            # Juste pour check ce qui se passe
            # print(node.value, node.children[word[0]].value, node.is_end, node.children[word[0]].is_end)
            radd(node.children[word[0]], word[1:])
        radd()
        
    def contains(self, word:str) -> bool:
        def rcontains(node=self.root, word:str=word):
            if not word: return False
            if node.children[word[0]].is_end and len(word) == 1: return True 
            return rcontains(node=node.children[word[0]], word=word[1:])
        return rcontains()
