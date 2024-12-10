class Solution:
    def maximumLength(self, s: str) -> int:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        candidates = []

        for key in mp:
            if mp[key] >= 3:
                candidates.append(key)
        if len(candidates) == 0:
            return -1
        elif len(candidates) == 1 and len(set(s)) == 1:
            return len(s) - 2

        #abdacbabd
        parsed_s = [i for i in s]
        
        i = 0
        longest_sub = 1
        sub = []
        ini = 0
        while i < len(s):
            if s[i] in candidates:
                sub.append(s[i])
                if len(sub) > 1:
                    tmp = 0
                    for j in range(len(s) - len(sub) + 1):
                        if sub == parsed_s[j:j + len(sub)]:
                            tmp += 1
                        if tmp == 3:
                            print(sub)
                            break
                    if tmp >= 3 and len(set(sub)) == 1:
                        longest_sub = max(len(sub), longest_sub)
                    else:
                        sub = []
            else:
                sub = []
            i += 1
        return longest_sub
                
                
                



