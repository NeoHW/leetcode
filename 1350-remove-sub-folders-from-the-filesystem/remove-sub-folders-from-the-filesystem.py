class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfPath = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, fs: str):
        curr = self.root
        parts = fs.split("/")
        for part in parts[1:]: # skip the empty part before first '/'
            part = '/' + part
            if part not in curr.children:
                curr.children[part] = TrieNode()
            curr = curr.children[part]
        curr.endOfPath = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f)
        
        res = []

        def dfs(node, path):
            if node.endOfPath:
                res.append(path)
                return
            
            for k, v in node.children.items():
                new_path = path + k
                dfs(v, new_path)

        dfs(trie.root, "")
        
        return res