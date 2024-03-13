# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        height = 0
        def recur(root, res, height):
            if root == None:
                return
            if len(res)==  height:
                res.append(root.val)

            # print(height)
            recur(root.right, res, height + 1)
            print(height)
            recur(root.left, res, height + 1)
            
        recur(root, res, height)
        return res

