class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node

            # search from given index to end of word
            for j in range(index, len(word)):
                char = word[j]

                if char == '.':
                    # need dfs backtrack
                    for child in curr.children.values():
                        if dfs(j+1, child): # if any path finds the word
                            return True
                    return False # when all paths fail
                else:
                    # normal searching of word
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.endOfWord

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)