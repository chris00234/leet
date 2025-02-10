class Solution:
    def clearDigits(self, s: str) -> str:
        li = [i for i in s]
        
        pop_count = 0
        for i in range(len(li) - 1, -1, -1):
            if li[i].isnumeric():
                li.pop(i)
                pop_count += 1
            elif pop_count > 0:
                li.pop(i)
                pop_count -= 1
        return "".join(li)
