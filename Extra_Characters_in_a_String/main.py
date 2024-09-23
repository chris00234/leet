class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_length = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word_length = len(word)

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        trie = Trie()
        self.buildTrie(trie, dictionary)
        
        dp = [-1] * len(s)
        return len(s) - self.dfs(s, trie.root, dp, 0)

    def buildTrie(self, trie: Trie, dictionary: list[str]):
        for word in dictionary:
            trie.insert(word)

    def dfs(self, s: str, node: TrieNode, dp: list[int], index: int) -> int:
        if index == len(s):
            return 0
        if dp[index] != -1:
            return dp[index]

        # Start with adding one extra character
        result = self.dfs(s, node, dp, index + 1)

        # Try to match words starting from current index
        currentNode = node
        for j in range(index, len(s)):
            if s[j] in currentNode.children:
                currentNode = currentNode.children[s[j]]
                if currentNode.word_length > 0:
                    result = max(result, currentNode.word_length + self.dfs(s, currentNode, dp, j + 1))
            else:
                break  # No more matches

        dp[index] = result
        return result
