class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        width = len(height) - 1
        area = 0

        while l < r:
            
            tmp = min(height[l],height[r]) * width
            if area < tmp:
                area = tmp
            if height[l] <= height[r]:
                l += 1
                width -= 1
            else:
                r -= 1
                width -= 1
        return area