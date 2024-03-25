class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = {}
        res = []
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                res.append(num)
        
        return res