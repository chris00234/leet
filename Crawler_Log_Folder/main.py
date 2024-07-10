class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = 0
        for cd in logs:
            if cd == "../":
                curr -= 1
                curr = max(0, curr)
            elif cd == "./":
                curr += 0
            else:
                curr += 1
        return curr
