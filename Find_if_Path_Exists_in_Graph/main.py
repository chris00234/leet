class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            if source == destination:
                return True
            return False
        mp = {}
        for edge in edges:
            if edge[0] not in mp:
                mp[edge[0]] = [edge[1]]
            else:
                mp[edge[0]].append(edge[1])
            if edge[1] not in mp:
                mp[edge[1]] = [edge[0]]
            else:
                mp[edge[1]].append(edge[0])
        stack = []
        for i in mp[source]:
            stack.append(i)
        visited = []
        visited.append(source)

        while stack:
            node = stack.pop(0)
            if node == destination:
                return True
            if node in visited:
                continue
            else:
                visited.append(node)
                for i in mp[node]:
                    stack.append(i)
        return False        
        

