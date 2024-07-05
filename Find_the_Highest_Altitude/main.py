class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        mx = 0
        for i in gain:
            prefix += i
            mx = max(mx, prefix)
        return mx
