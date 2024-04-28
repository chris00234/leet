class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        count = [1]*n
        ans = [0]*n

        for x, y in edges:
            tree[x].add(y)
            tree[y].add(x)
        
        print(tree)

        def dfs(node, parent, flag=True):
            for child in tree[node]:
                if flag and child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
                
                if not flag and child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs(child, node, False)
                    
        dfs(0, None)
        dfs(0, None, False)
        

	return ans






