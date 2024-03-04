class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            if tokens[0] > power:
                return 0
            else:
                return 1
        
        tokens.sort()
        score = 0
        last = len(tokens) - 1
        first = 0

        while first != last:
            if score <= 0:
                if power >= tokens[first]:
                    power -= tokens[first]
                    first += 1
                    score += 1
                else:
                    return 0
            else:
                if power >= tokens[first]:
                    power -= tokens[first]
                    first += 1
                    score += 1
                else:
                    power += tokens[last]
                    last -= 1
                    score -= 1
            print(power)

        if first == last:
            if tokens[first] <= power:
                score += 1

        print(tokens)
        return score