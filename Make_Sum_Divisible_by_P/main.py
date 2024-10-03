class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)  # Calculate total sum of the array
        remainder = total_sum % p  # Find the remainder when total sum is divided by p

        # If the total sum is already divisible by p, return 0 (no subarray needs to be removed)
        if remainder == 0:
            return 0

        def find_smallest_subarray(nums, p, remainder):
            prefix_sum = 0
            min_length = len(nums)  # Initialize the minimum length of the subarray
            prefix_map = {0: -1}  # Store prefix sums modulo p with their indices

            for i, num in enumerate(nums):
                prefix_sum += num
                target_remainder = (prefix_sum % p - remainder) % p

                # If target_remainder exists in prefix_map, calculate subarray length
                if target_remainder in prefix_map:
                    min_length = min(min_length, i - prefix_map[target_remainder])

                # Update prefix_map with the current prefix_sum % p
                prefix_map[prefix_sum % p] = i

            return min_length

        smallest_subarray_length = find_smallest_subarray(nums, p, remainder)

        # If smallest_subarray_length is equal to the array length, return -1, otherwise return it
        return smallest_subarray_length if smallest_subarray_length < len(nums) else -1
