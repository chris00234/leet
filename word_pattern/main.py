class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        parse = s.split()
        d = {i: None for i in pattern}
        if len(pattern) != len(parse):
            return False
    
        for lt in range(len(pattern)):
            if d[pattern[lt]] == None:
                if parse[lt] in d.values():
                    return False
                d[pattern[lt]] = parse[lt]
            else:
                if d[pattern[lt]] != parse[lt]:
                    print(d[pattern[lt]])
                    return False
        return True 