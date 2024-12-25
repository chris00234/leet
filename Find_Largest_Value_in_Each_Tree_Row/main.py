# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ret = []

        layer = []
        layer.append([root])
        ret.append([root.val])
        t = 0

        
        while len(layer) != 0:
            nodes = layer.pop()
            tmp = []
            ret_tmp = []
            while len(nodes) != 0:
                node = nodes.pop()
                if node.left:
                    print(node.left.val)
                    tmp.append(node.left)
                    ret_tmp.append(node.left.val)
                if node.right:
                    print(node.right.val)
                    tmp.append(node.right)
                    ret_tmp.append(node.right.val)
            if len(tmp) != 0:
                layer.append(tmp)
                ret.append(ret_tmp)
        
        ans = []
        for item in ret:
            ans.append(max(item))
        return ans
        

        
