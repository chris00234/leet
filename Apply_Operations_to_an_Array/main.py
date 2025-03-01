class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # First pass: Apply the doubling operation
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Second pass: Shift non-zero elements to the left, keeping order
        non_zero_elements = [num for num in nums if num != 0]  # Extract non-zero elements
        zero_count = len(nums) - len(non_zero_elements)  # Count zeros
        result = non_zero_elements + [0] * zero_count  # Append zeros at the end
        
        return result
