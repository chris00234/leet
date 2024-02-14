class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        count = 0
        last_val = 0
        for i in range(len(citations)):
            if i <= citations[i]:
                count += 1
                last_val = citations[i]
            else:
                break
        if last_val <= count:
            return last_val
        return count
            
