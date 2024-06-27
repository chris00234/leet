class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        li = [0 for _ in range(len(edges) + 1)]

        for edge in edges:
            li[edge[0] - 1] += 1
            li[edge[1] - 1] += 1
        
        index = 1
        mx = 0
        for _ in range(len(li)):
            if mx < li[_]:
                mx = li[_]
                index = _ + 1
        return index
                
