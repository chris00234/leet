class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heapify(nums)
        for _ in range(len(nums)):
            res.append(heappop(nums))

        return res


