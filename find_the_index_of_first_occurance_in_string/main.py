class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        same = True
        store = -1
        pos = 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                store = i
                pos = i + 1
                for j in range(1, len(needle)):
                    print(pos)
                    if pos < len(haystack):
                        if needle[j] != haystack[pos]:
                            same = False
                            break
                        else:
                            same = True
                    else:
                        return -1
                    pos += 1
                if same == True:
                    return store
        print("------")
        return -1