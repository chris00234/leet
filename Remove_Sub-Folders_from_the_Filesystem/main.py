class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
 
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for path in folder:
            node = root
            for ch in path.split('/'):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end_of_word = True


        def bt(node, path):
            if node.is_end_of_word:
                return ['/'.join(path)]
            ans = []
            for ch in node.children:
                path.append(ch)
                ans += bt(node.children[ch], path)
                path.pop()
            return ans

        return bt(root, [])
