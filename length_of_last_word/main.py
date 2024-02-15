class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = ""
        li = []
        for char in s:
            if char != ' ':
                st += char
            else:
                if st != "":
                    li.append(st)
                st = ""
        if st != "":
            li.append(st)
        # print(li)
        return len(li[-1])
        