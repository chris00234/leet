class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        length = m + n
        
        for i in range(length):
            if i < m:
                pass
            else:
                nums1[i] = 0
        
        i = 0
        j = 0
        
        while True:
            if j >= (n) or i >= (length):
                break
            num1 = nums1[i]
            num2 = nums2[j]
            # print(num1, num2)
            if num1 <= num2:
                if num1 == 0:
                    nums1[i] = num2
                    i += 1
                    j += 1
                else:
                    i += 1
            else:
                if num1 != 0:
                    nums1.insert(i - 1, num2)
                    i += 1
                    j += 1
        
        for i in range(length, len(nums1)):
            nums1.pop()
      


if __name__ == '__main__':
    ans = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    
    ans.merge(nums1, m, nums2, n)
    print(nums1)        