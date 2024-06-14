class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        cntArray = [0]*(max(nums)+1)

        for num in nums:
            cntArray[num] += 1

        duplicatStack = []
        move = 0
        for i in range(len(cntArray)):
            if cntArray[i] >= 1:
                while cntArray[i] != 1:
                    duplicatStack.append(i)
                    cntArray[i] -= 1
            else:
                if len(duplicatStack) > 0:
                    move += i - duplicatStack.pop()
        
        value = max(nums) + 1
        while len(duplicatStack)!=0:
            move += value -duplicatStack.pop()
            value+=1
        
        return move
