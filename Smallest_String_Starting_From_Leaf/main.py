# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_string = '{'
        def dfs(node, path):
            nonlocal smallest_string
            if node:
                path.append(chr(ord('a') + node.val))
                if node.left is None and node.right is None:
                    curr = ''.join(reversed(path))
                    print(curr, smallest_string)
                    smallest_string = min(curr, smallest_string)
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()
        dfs(root, [])
        return smallest_string
