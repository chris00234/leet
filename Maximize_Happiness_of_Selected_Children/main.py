class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness, key= lambda x: x, reverse= True)
        sum_child = 0
        num = 0
        for i in range(k):
            sum_child += sorted_happiness[i] - num if sorted_happiness[i] - num > 0 else 0
            num += 1
            
        return sum_child

