class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        li = []
        while x > 0:
            md = x % 10
            x = x // 10
            li.append(md)
        l = 0
        r = len(li) - 1

        while l < r:
            if li[l] != li[r]:
                return False
            l += 1
            r -= 1
        return True
