# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def recur(node):
            nonlocal ans
            if not node:
                return 0
            
            if node.left:
                tmp = node.left
                if not tmp.left and not tmp.right:
                    ans += tmp.val
                    print(ans)
            
            recur(node.left)
            recur(node.right)
            
            

        recur(root)
        return ans
        
        

