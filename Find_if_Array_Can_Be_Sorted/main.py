class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if sorted(nums) == nums:
            return True
        seg = []
        prev = self.checkbits(nums[0])
        tmp = []
        bit = 0
        for num in nums:
            if num == nums[0]:
                tmp.append(num)
                bit = self.checkbits(num)
            elif bit == self.checkbits(num):
                tmp.append(num)
            elif bit != self.checkbits(num):
                bit = self.checkbits(num)
                seg.append(tmp)
                tmp = []
                tmp.append(num)
            if num == nums[-1] and tmp not in seg:
                seg.append(tmp)
        if len(seg) == 1:
            return True
        print(seg)
        for i in range(len(seg) - 1):
            if max(seg[i]) > min(seg[i+1]):
                return False
        return True

        
    

    def checkbits(self, num):
        ret = str(bin(num))
        count = 0
        for ch in ret:
            if ch == '1':
                count += 1
        return count
