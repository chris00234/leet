class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largest = -1
        

        for num in nums:
            if num > largest and -num in nums:
                largest = num

        return largest
                
