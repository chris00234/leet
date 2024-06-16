class Solution:
    def minPatches(self, nums, n):
        patches = reachable = 0
        for num in nums:
            while reachable < min(num - 1, n):
                reachable +=  reachable + 1
                patches += 1
            reachable += num
        
        while reachable < n:
            reachable = 2 * reachable + 1
            patches += 1 
        
        #print(reachable)
        return patches
