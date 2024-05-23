class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        banned = set()
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ban = (1 << j) + (1 << i)
                    banned.add(ban)
                    
        for i in range(1, (1 << n)):
            s = set()
            flag = True
            for ban in banned:
                if (ban & i) == ban:
                    flag = False
            if flag:
                count += 1
        
        return count
