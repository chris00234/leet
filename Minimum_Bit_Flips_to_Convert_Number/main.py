class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bnStart = str(bin(start))[2:]
        bnGoal = str(bin(goal))[2:]
        diff = len(bnStart) - len(bnGoal)
        if diff > 0:
            while diff:
                bnGoal = "0" + bnGoal
                diff -= 1
        elif diff < 0:
            while diff:
                bnStart = "0" + bnStart
                diff += 1
        
        ret = 0

        for c in range(len(bnGoal)):
            if bnStart[c] != bnGoal[c]:
                ret += 1
        return ret





        
