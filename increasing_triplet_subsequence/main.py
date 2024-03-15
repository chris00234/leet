class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        uniq = set(nums)
        if len(uniq) < 3:
            return False
        i = nums[0]
        j = nums[1]
        k = nums[2]
        ipos = 0
        jpos = 1
        kpos = 2
        if i < j < k:
            return True
        
        while kpos < len(nums) -1:
            if i < j:
                if j >= k:
                    kpos += 1
                    k = nums[kpos]
                else:
                    return True
            elif i >= j:
                if jpos - ipos > 1:
                    ipos += 1
                    i = nums[ipos]
                else:
                    ipos += 1
                    jpos += 1
                    kpos += 1
                    i = nums[ipos]
                    j = nums[jpos]
                    k = nums[kpos]
            # print(i,j,k)    
            if i < j and j < k:
                # print("here")
                return True    
            if kpos == len(nums) -1:
                jpos += 1
                kpos = jpos + 1
                j = nums[jpos]
                if kpos < len(nums):
                    k = nums[kpos]
            if i < j and j < k:
                # print("here")
                return True   
           
        return False
                
            