class Solution:
    def reverseVowels(self, s: str) -> str:
        checker = ['a', 'e', 'i', 'o', 'u']

        l = 0
        r = len(s) - 1
        li = []
        for char in s:
            li.append(char)


        while l < r:
            if li[l].lower() not in checker:
                l += 1
            elif li[r].lower() not in checker:
                r -= 1
            # print(l, r)
            if li[l].lower() in checker and li[r].lower() in checker:
                li[l], li[r] = li[r], li[l]
                l += 1
                r -= 1
            
        
        return "".join(li)
