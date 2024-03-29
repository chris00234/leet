class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        val = max(nums)
        l, r, count, ans = 0,0,0,0

        while r < n:
            if nums[r] == val:
                count += 1
            
            if count >= k:
                while count >= k:
                    ans += n - r
                    if nums[l] == val:
                        count -= 1
                    l += 1
            r += 1
        
        return ans
        # val = max(nums)
        # l,r = 0,0
        # ans = 0
        # mp = {}

        # for r in range(len(nums)):
        #     mp[nums[r]] = mp.get(nums[r], 0) + 1
        #     while mp[nums[r]] >= k:
        #         ans += len(nums) - r
        #         mp[nums[l]] -= 1
        #         l += 1
                
           
            
        
        # print(mp)
        # return ans
