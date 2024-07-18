
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            for el in left:
                for er in right:
                    if el + er <= distance:
                        self.ans += 1
                        
            return [l + 1 for l in left + right if l < distance]
        
        self.ans = 0 
        dfs(root)
        return self.ans
