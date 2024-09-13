class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ret = []
        mp = {}
        for query in queries:
            val = 0
            if mp.get(str(query)) == None:
                for i in range(query[0], query[1] + 1):
                    val ^= arr[i]
                mp[str(query)] = val
            else:
                val = mp.get(str(query))
            ret.append(val)

        return ret
