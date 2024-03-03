# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxval = 0
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, currMax):
            if not node:
                return 0
            if node.val >= currMax:
                cnt = 1
            else:
                cnt = 0
            currMax = max(currMax, node.val)
            cnt += helper(node.left, currMax)
            cnt += helper(node.right, currMax)
            return cnt
        return helper(root, root.val)

         
        
        