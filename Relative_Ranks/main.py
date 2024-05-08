class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, key = lambda x: x, reverse = True)
        print(sorted_score)
        dic = {}
        pos = 1
        for n in sorted_score:
            dic[n] = pos
            pos += 1
        
        for i in range(len(score)):
            val = dic[score[i]]
            if val == 1:
                score[i] = 'Gold Medal'
            elif val == 2:
                score[i] = 'Silver Medal'
            elif val == 3:
                score[i] = 'Bronze Medal'
            else:
                score[i] = str(val)
        return score
