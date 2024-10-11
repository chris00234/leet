import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Min-heap to track the smallest unoccupied chair
        nextChair = 0
        targetStart = times[targetFriend][0]

        # Sort the times array by arrival times
        times.sort()
        # Min-heap for tracking friends who have left (leave_time, chair_number)
        leave_chair = []  # (leaveTime, chair)
        # Min-heap for available chairs
        available_chairs = []

        # Iterate through each friend's arrival and leaving times
        for start, leave in times:
            # Free up chairs for friends who have already left before the current arrival
            while leave_chair and leave_chair[0][0] <= start:
                # Push the vacated chair back into available chairs
                heapq.heappush(available_chairs, heapq.heappop(leave_chair)[1])
            
            # Assign the smallest available chair or the next new chair
            if available_chairs:
                sat = heapq.heappop(available_chairs)
            else:
                sat = nextChair
                nextChair += 1
            
            # Add this friend's leaving time and the chair they occupy to the leave_chair heap
            heapq.heappush(leave_chair, (leave, sat))

            # If this is the target friend, return their chair number
            if start == targetStart:
                return sat

        return -1 # Default case (should never reach here)
