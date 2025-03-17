class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key in dic:
            if dic[key] % 2 != 0:
                return False
        return True
