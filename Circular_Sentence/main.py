class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ret = True
        li = sentence.split(" ")

        if len(li) == 1:
            if li[0][0] != li[0][-1]:
                return False
            return True

        first_char = li[0][0]
        prev = ""
        for el in li:
            if prev == "":
                prev = el[-1]
            else:
                if prev != el[0]:
                    return False
            prev = el[-1]
        
        if prev == first_char:
            return True
        return False
