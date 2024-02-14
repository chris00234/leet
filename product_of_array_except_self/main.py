class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        pre = 1
        post = 1
        length = len(nums)
        for i in range(length):
            result[i] = pre
            pre *= nums[i] 
        
        #result = 1, 1, 2, 6
        print(result)

        for i in range(length -1, -1, -1):
            result[i] *= post
            post *= nums[i]
            print(f'{i} = {result[i]}')
        
        #result =  24  24   12  6
        return result