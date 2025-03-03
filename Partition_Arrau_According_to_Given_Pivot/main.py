class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_li = []
        pivot_li = []
        greater_li = []

        for num in nums:
            if num < pivot:
                less_li.append(num)
            elif num == pivot:
                pivot_li.append(num)
            else:
                greater_li.append(num)

        return less_li + pivot_li + greater_li

