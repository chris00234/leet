class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = len(nums) - 1
        result = 0
        i = 0
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    tmp = nums[j]
                    nums[j] = '_'
                    nums[i] = tmp
                    j -= 1
                    result += 1
                    i += 1
                else:
                    if j == i:
                        nums[i] = '_'
                        result += 1
                    else:
                        nums[j] = '_'
                        result += 1
                    j -= 1
                    
                    continue
            else:
                i += 1
        return nums
            

if __name__ == '__main__':

    ans = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(ans.removeElement(nums, val))