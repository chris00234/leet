class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_index = -1
        max_index = -1
        curl = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                curl = i
            if nums[i] == minK:
                min_index = i
            if nums[i] == maxK:
                max_index = i
            print(curl, min_index, max_index)
            smaller = min(min_index, max_index)
            tmp = smaller - curl
            if tmp <= 0:
                ans += 0
            else:
                ans += tmp
        return ans
