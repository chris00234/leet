class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dict_ = {}
        for road in roads:
            dict_[road[0]] = dict_.get(road[0], 0) + 1
            dict_[road[1]] = dict_.get(road[1], 0) + 1

        dic = sorted(dict_.items(), key=lambda item: item[1], reverse=True)
        for key in dic:
            dict_[key[0]] = n
            n -= 1
        
        ret = 0
        for road in roads:
            ret += dict_[road[0]] + dict_[road[1]]
        return ret

