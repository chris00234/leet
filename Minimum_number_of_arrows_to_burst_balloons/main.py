class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key= lambda x: x[1])
        def in_range(point, x):
            return True if point[0] <= x <= point[1] else False
        res = 1
        new_point = False
        x = sorted_points[0][1]
        for point in sorted_points:
            new_point = in_range(point, x)
            print(point, x, new_point)
            if new_point == False:
                x = point[1]
                res += 1
            
        
        return res
