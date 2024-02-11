class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num_dict = {}
        
        for element in nums:
            if element not in num_dict:
                num_dict[element] = 0
            num_dict[element] += 1
        
        max_val = 0
        result = 0
        for key,value in num_dict.items():
            if max_val < value:
                max_val = value
                result = key
        
        print(result)
        
        


li = [3,2,3]
ans = Solution()
ans.majorityElement(li)