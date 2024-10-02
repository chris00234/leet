class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mp = {}
        li = arr.copy()
        arr.sort()
        pos = 1
        for i in arr:
            if mp.get(i, 0) == 0:
                mp[i] = pos
                pos += 1
        
    
        ret = []

        for k in li:
            ret.append(mp[k])
        return ret
