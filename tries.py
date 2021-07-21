class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current = self.root

        for char in word:
            # If the character is in the children, follow it
            try:
                #print (f"{char} -> {current.children.keys()}")
                current = current.children[char]
            except KeyError:
                return None

        return current

    def insert(self, word):
        current = self.root
        for char in word:
            # If the character is in the children, follow it
            try:
                current = current.children[char]
            except KeyError:
                # If the current character isn't found, add a new node
                new = TrieNode()
                current.children[char] = new

                # Follow the new node
                current = new

        # Add an * at the end of the word
        current.children["*"] = None

    def get_possible_words(self, node=None, word="", words=[]):
        # Current node is root or node passed in arguements
        current = node or self.root

        # Go through each of the node's children
        # .items gets array of key and value pairs
        for key, child in current.children.items():
            # If the current key is * it means its at the end of a complete word
            if key == "*":
                words.append(word)
            else:
                # Recursively call function on child node
                self.get_possible_words(child, word + key, words)
        return words

    def autocomplete(self, prefix):
        current = self.search(prefix)
        if not current:
            return None
        return self.get_possible_words(current)

## Example ##
a = Trie()
a.insert("apples")
a.insert("bananas")
a.insert("pears")

# Gets autocomplete for ba (It is bananas)
print (a.autocomplete("ba"))
