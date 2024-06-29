class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        rank = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]

        #build graph
        for source, dest in edges:
            graph[source].append(dest)
            rank[dest] += 1


        Q = collections.deque()
        for i in range(len(rank)):
            if rank[i] == 0:
                Q.append(i)

        #explore
        ancestry = [set() for _ in range(n)]

        while Q:
            curParent = Q.popleft()

            for child in graph[curParent]:
                ancestry[child].add(curParent)
                ancestry[child].update(ancestry[curParent])

                rank[child] -= 1
                if rank[child] == 0:
                    Q.append(child)


        result = [sorted(setObj) for setObj in ancestry]

        return result

