class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        mid = 0
        if target > nums[j]:
            return j + 1
        if target < nums[i]:
            return 0
        while i <= j:
            mid = int((i + j)/2)
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1
            else:
                return mid
            
        
        return i 