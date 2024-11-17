class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        shortest = float('inf')  # Track shortest valid subarray length
        queue = deque([])        # Store (sum, length) pairs
        total = currLen = 0      # Track current sum and length
        
        for i, n in enumerate(nums):
            if n < 0:
                # Handle neg. numbers
                if total + n <= 0:
                    queue = deque([])
                    total = currLen = 0
                    continue
                else:
                    removed, removeLen = queue.pop()  # Merge neg. numb 
                    curr = n + removed
                    stackLength = 1 + removeLen
                    
                    while queue and curr < 0: # Keep merging non-neg. sum
                        removed, removeLen = queue.pop()
                        curr += removed
                        stackLength += removeLen
                    
                    total += n
                    queue.append((curr, stackLength))
                    currLen += 1
            else:
                queue.append((n, 1)) # Handle pos. numb
                total += n
                currLen += 1
            
            while queue and total >= k: # Check if cur. window sum exceeds k
                shortest = min(shortest, currLen)
                removed, removeLen = queue.popleft()
                total -= removed
                currLen -= removeLen
        
        return shortest if shortest <= len(nums) else -1
