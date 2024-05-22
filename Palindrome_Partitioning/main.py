class Solution:
    def partition(self, s: str) -> List[List[str]]:
        print(s[::-1])
        res = []
        def dfs(l, final):
            if not l:
                res.append(final)
                return
            for i in range(len(l)):
                if l[:i+1] == l[:i+1][::-1]:
                    dfs(l[i+1:], final + [l[:i+1]])
        dfs(s,[])
        return res
