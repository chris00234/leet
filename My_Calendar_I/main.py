class MyCalendar:
    def __init__(self):
        # Define the slots in the calendar
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        # The index of this time slots if it is booked
        index = bisect.bisect_left(self.slots, (start, end))
        res = True

        # Check the next time slot 
        # which will be the current index if it is existed
        if index < len(self.slots): res &= end <= self.slots[index][0]
        
        # Check the previous time slot 
        # which will be the index - 1 if it is existed  
        if index - 1 >= 0: res &= start >= self.slots[index-1][1]

        # Only insert if it satisfied previous and next time slot
        if res: bisect.insort_left(self.slots, (start, end))
        return res

