class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def formTrie(self, keys):
        for key in keys:
            self.insert(key) 

    def insert(self, key):
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestionsRec(self, node, word):
        if node.last:
            print(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):
        node = self.root

        for a in key:
            if not node.children.get(a):
                return 0
            node = node.children[a]
        if not node.children:
            return -1

        self.suggestionsRec(node, key)
        return 1


keys = open("dictionary.txt", "r")
key = input("enter the word")


t = Trie()

t.formTrie(keys)
comp = t.printAutoSuggestions(key)

if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")