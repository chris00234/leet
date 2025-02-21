# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        def dfs(root):
            if root == None:
                return
            if root.left != None:
                root.left.val = root.val * 2 + 1
            if root.right != None:
                root.right.val = root.val * 2 + 2
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        self.root = root

    def find(self, target: int) -> bool:
        def dfs(root):
            if root is None:
                return False
            if root.val == target:
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
