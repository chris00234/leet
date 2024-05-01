class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        ret = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                ret.append(True)
            else:
                ret.append(False)
        return ret
