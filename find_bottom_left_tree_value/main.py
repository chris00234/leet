# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        visited = []
        stack = []
        stack.append(root)
        tmp = stack[-1]
        height = 0
        max_height = 0
        result = 0
        if root.left == None and root.right == None:
            return root.val

        while len(stack) != 0:
            if tmp.left != None and tmp.left not in visited:
                stack.append(tmp.left)
                tmp = stack[-1]
                height += 1
            elif tmp.right != None and tmp.right not in visited:
                stack.append(tmp.right)
                tmp = stack[-1]
                height += 1
            else:
                tmp = stack[-1]
                visited.append(tmp)
                if tmp.right != None and tmp.right not in visited:
                    continue
                if tmp.left != None and tmp.left not in visited:
                    continue
                stack.pop()
                if height > max_height:
                    max_height = height
                    result = tmp.val
                print(height)
                height -= 1
                
                # print(tmp.val)
                
        return result
        
        