# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val %2 == 0:
            return False
        queue = []
        queue.append(root)
        tmp = []
        level = 0
        import copy
        while queue:
            level += 1
            while queue:
                node = queue.pop(0)
                if node.left != None:
                    tmp.append(node.left)
                if node.right != None:
                    tmp.append(node.right)
            queue = copy.copy(tmp)
            for i in queue:
                print(i.val)
            print('-------')
            if level % 2 == 1:
                if len(tmp) == 1:
                    if tmp[0].val %2 == 1:
                        return False
                for i in range(len(tmp) - 1):
                    if tmp[i].val > tmp[i + 1].val:
                        if tmp[i].val % 2 == 0 and tmp[i + 1].val % 2 == 0:
                            pass
                        else:
                            return False
                    else:
                        return False
            else:
                if len(tmp) == 1:
                    if tmp[0].val %2 == 0:
                        return False
                for i in range(len(tmp) - 1):
                    if tmp[i].val < tmp[i + 1].val:
                        if tmp[i].val % 2 == 1 and tmp[i + 1].val % 2 == 1:
                            pass
                        else:
                            return False
                    else:
                        print('here')
                        return False        
            tmp.clear()
            

        return True

      
            
        
                  