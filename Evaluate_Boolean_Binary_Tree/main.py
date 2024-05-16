# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return root.val
        ans = 0
        def dfs(node):
            nonlocal ans
            if node.left == None and node.right == None:
                return bool(node.val)
            
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)
            
            
        return dfs(root)
                    
        
            

