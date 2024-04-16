# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        d = 1
        if depth == 1:
            new_node = TreeNode(val, root, None)
            root = new_node
        stack = []
        tmp = root
        stack.append(tmp)
        while d <= depth:
            if depth - 1 == d:
                print([i.val for i in stack])
                while stack:
                    curr = stack.pop(0)
                    l = curr.left
                    r = curr.right
                    if not l and not r:
                        curr.left = TreeNode(val, None, None)
                        curr.right = TreeNode(val, None, None)
                    if l:
                        curr.left = TreeNode(val, l, None)
                    elif not l:
                        curr.left = TreeNode(val, None, None)
                    if r:
                        curr.right = TreeNode(val, None, r)
                    elif not r:
                        curr.right = TreeNode(val, None, None)
                    
                break
            else:
                li = []
                while stack:
                    node = stack.pop(0)
                    if node.left != None:
                        li.append(node.left)
                    if node.right != None:
                        li.append(node.right)
                stack = li
                d += 1
        return root

