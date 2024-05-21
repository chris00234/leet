class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        index = 0
        def recur(nums, subset, index, res):
            res.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                recur(nums, subset, i + 1, res)
                subset.pop()
        recur(nums, subset, index, res)
        return res

        

