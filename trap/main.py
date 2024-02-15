class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Initialize arrays l and r to store the maximum height to the left and right of each bar.
        l = [0] * n  
        r = [0] * n
        ans = 0
        lm, rm = 0, 0

        # Iterate from left to right and populate l array.
        for i in range(n):
            l[i] = lm
            if lm < height[i]:
                lm = height[i]

        # Iterate from right to left and populate r array.
        for i in range(n - 1, -1, -1):
            r[i] = rm
            if rm < height[i]:
                rm = height[i]

        # Iterate through the array to calculate trapped water.
        for i in range(n):
            # Calculate the trapped water at each position.
            trapped = min(l[i], r[i]) - height[i]
            if trapped > 0:
                ans += trapped

        return ans