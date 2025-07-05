class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ret = []
        for key in counter:
            if key == counter[key]:
                ret.append(key)
        return max(ret) if len(ret) > 0 else -1
