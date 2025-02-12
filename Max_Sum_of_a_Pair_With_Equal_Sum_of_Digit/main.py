class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            sm = 0
            tmp = num
            while num > 0:
                digit = num % 10
                num //= 10
                sm += digit
            if sm not in dic:
                dic[sm] = []
                dic[sm].append(tmp)
            else:
                dic[sm].append(tmp)
        ret = -1
        for key in dic:
            if len(dic[key]) > 1:
                temp = max(dic[key])
                max_idx = dic[key].index(temp)
                dic[key].pop(max_idx)
                temp += max(dic[key])
                ret = max(ret, temp)
        return ret
