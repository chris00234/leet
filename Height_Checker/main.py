class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights, key = lambda x: x)
        ret = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                ret += 1
        return ret
