class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        rest = ""
        tmp = s
        tmp = list(tmp)
        print(tmp)
        for letter in order:
            while letter in tmp:
                result += letter
                tmp.remove(letter)

        
        for i in tmp:
            rest += i
        return result + rest

