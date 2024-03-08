class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}

        for i in nums:
            if i in hash_map.keys():
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        max_val = 0
        for val in hash_map.values():
            if val > max_val:
                max_val = val
        
        result = 0
        for val in hash_map.values():
            if val == max_val:
                result += val
        return result
