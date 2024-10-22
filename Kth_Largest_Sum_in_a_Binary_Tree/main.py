# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]
        li = []
        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            li.append(level)
        ret = [sum(x) for x in li]
        ret.sort()
        return ret[k * -1] if len(ret) >= k else -1
