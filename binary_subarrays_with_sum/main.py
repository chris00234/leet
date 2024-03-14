class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict={0:1}
        res=0
        sum=0
        for i in nums:
            sum+=i
            res+=dict.get(sum-goal,0)
            dict[sum]=dict.get(sum,0)+1
        return res

        #dict[1] = 2. res = 1
        #dict[2] = 2