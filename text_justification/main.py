import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = 0
        i = 0
        initial_ind = 0
        result = []
        while i < len(words):
            length += len(words[i]) + 1
            if length > maxWidth:
                length -= 1
            if length > maxWidth:
                length -= len(words[i])
                i = i - 1 # because going backward once.
                # do from init to i + 1...
                st = ""
                word_count = 0
                for j in range(initial_ind, i + 1):
                    st += words[j]
                    word_count += 1
                    # think about padding
                print(len(st))
                print(word_count)
                space_needed = maxWidth - len(st)
                space_count = word_count - 1
                if space_count != 0:
                    space_val = space_needed / space_count
                    padd = False
                    if space_needed % space_count != 0:
                        padd = True
                    ans = ""
                    for j in range(initial_ind, i + 1):
                        ans += words[j]
                        if j != i:
                            if padd:
                                ans += (" " * math.ceil(space_val))
                                space_needed -= math.ceil(space_val)
                                space_count -= 1
                                if space_needed % space_count != 0:
                                    padd = True
                                else:
                                    padd = False
                            else:
                                ans += (" " * math.floor(space_val))
                else:
                    print("hereeee")
                    space_val = space_needed
                    ans = ""
                    for j in range(initial_ind, i +1):
                        ans += words[j]
                        ans += " " * space_val
                    print(ans)


                result.append(ans)

                # result.append(st)
                length = 0
                initial_ind = i + 1
            i += 1

            if i == len(words):
                st = ""
                word_count = 0
                for j in range(initial_ind, i):
                    st += words[j]
                    word_count += 1
                
                space_needed = maxWidth - len(st)
                space_count = word_count - 1

                if space_count != 0:
                    space_val = space_needed / space_count
                    padd = False
                    if space_needed % space_count != 0:
                        padd = True
                    ans = ""
                    wc = maxWidth
                    for j in range(initial_ind, i):
                        wc -= len(words[j])
                        ans += words[j]
                        if len(ans) != maxWidth:
                            ans += (" ")
                        wc -= 1

                    ans += (" " * wc)
                else:
                    space_val = space_needed
                    ans = ""
                    for j in range(initial_ind, i):
                        ans += words[j]
                        ans += " " * space_val
                result.append(ans)
                print(len(st))
                # print(word_count)
                    # think about padding
                # result.append(st)
        return result