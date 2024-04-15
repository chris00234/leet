# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        li = []
        ans = 0
        def recur(root):
            nonlocal li
            nonlocal ans
            if not root:
                return
            li.append(root.val)
            if not root.left and not root.right:
                tmp = 0
                for i in li:
                    tmp = tmp*10 + i
                ans += tmp
                
            
            recur(root.left)
            recur(root.right)
            li.pop()

        recur(root)
        return ans
