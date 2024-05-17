# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left:
                if node.left.left == None and node.left.right == None and node.left.val == target:
                    node.left = None
            if node.right:
                if node.right.left == None and node.right.right == None and node.right.val == target:
                    node.right = None

        dfs(root)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root
        
