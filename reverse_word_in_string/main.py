class Solution:
    def reverseWords(self, s: str) -> str:
        li = []
        st = ""

        for char in s:
            if char != " ":
                st += char
            if char == " ":
                if st != "":
                    li.append(st)
                st = ""
        if st != "":
            li.append(st)
        
        st = ""
        
        for i in range(len(li) - 1, -1, -1):
            st += li[i] + " "

        st = st[:-1]

        return st
        