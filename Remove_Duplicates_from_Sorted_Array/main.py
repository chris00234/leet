prev = nums[0]
        index = 1
        for i in range(1, len(nums)):
            if prev != nums[i]:
                nums[index] = nums[i]
                prev = nums[i]
                index += 1
        return index
