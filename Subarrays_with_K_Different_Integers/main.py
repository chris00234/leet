class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper (n, k, nums):
            l,r = 0,0
            mp = {}
            ans = 0
            n = len(nums)

            while r < n:
                mp[nums[r]] = mp.get(nums[r], 0) + 1
                while len(mp) > k:
                    mp[nums[l]] -= 1
                    if mp[nums[l]] == 0:
                        del mp[nums[l]]
                    l += 1
                ans += r - l + 1
                r += 1
            
            return ans
        return helper(len(nums), k , nums) - helper(len(nums), k - 1, nums)
