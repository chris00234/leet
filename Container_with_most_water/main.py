'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''



class Solution:
    def get_area(self, left, right, width):
        if left >= right:
            return right*width
        else:
            return left * width
        
    def maxArea(self, height: list[int]) -> int:
        width = len(height) - 1
        left = height[0]
        right = height[width]
        max_container = self.get_area(left, right, width)
        
        offset = 1
        current_left_ind = 0
        current_right_ind = width
        container = 0
        while current_left_ind < len(height) - 1 and current_right_ind > 0:
            current_left_ind += offset
            current_right_ind -= offset
            if height[current_left_ind] - left >= 2:
                left = height[current_left_ind]
                width -= 1
                container = self.get_area(left, right, width)
            elif height[current_right_ind] - right >= 2:
                width -= 1
                right = height[current_right_ind]
                container = self.get_area(left, right, width)
            
            if container > max_container:
                max_container = container
        return max_container