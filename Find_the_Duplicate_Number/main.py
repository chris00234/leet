class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}

        for num in nums:
            if num in mp:
                return num
            else:
                mp[num] = 1
        
        