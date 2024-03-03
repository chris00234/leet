# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        li1 = []
        li2 = []
        def store(root, li):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                li.append(root.val)
                return 0
            return store(root.left, li) + store(root.right, li)
        store(root1, li1)
        store(root2, li2)
        print(li1, li2)
        if len(li1) != len(li2):
            return False
        for i in range(len(li1)):
            if li1[i] != li2[i]:
                return False
        return True
