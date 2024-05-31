class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict_ = {}
        for num in nums:
            dict_[num] = dict_.get(num, 0) + 1

        ret = []
        print(dict_)

        for key in dict_:
            if dict_[key] == 1:
                ret.append(key)

        return ret
