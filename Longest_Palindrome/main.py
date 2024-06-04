class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_ = {}
        ret = 0
        odd = False
        for ch in s:
            dict_[ch] = dict_.get(ch, 0) + 1
        print(dict_)
        print(len(s))
        for key in dict_:
            if dict_[key] % 2 == 0:
                ret += dict_[key]
            else:
                ret += dict_[key] - 1
                odd = True
            
        return ret + 1 if odd else ret
