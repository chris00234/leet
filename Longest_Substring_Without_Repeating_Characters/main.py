class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        sub_str = ""
        if s == "":
            return 0
        for i in range(len(s)):
            sub_str = ""
            sub_str += s[i]
            count = 0
            count += 1
            for j in range(i + 1, len(s)):
                if s[j] not in sub_str:
                    sub_str += s[j]
                    count += 1
                    if count > result:
                        result = count
                    
                else:
                    break
            
        return 1 if result == 0 else result