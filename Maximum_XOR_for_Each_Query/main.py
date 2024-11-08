class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ret = []
        prefix = 0
        for num in nums:
            prefix ^= num
            ret.append((2 ** maximumBit - 1) ^ prefix)
            
        return ret[::-1]
            

