class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}

        for el in arr:
            dic[el] = dic.get(el, 0) + 1
        
        li = []
        for key, val in dic.items():
            li.append(val)
        li.sort()
        ret = len(dic)
        while k > 0:
            k -= li[0]
            li.pop(0)
            if k < 0:
                break
            ret -= 1
        return ret

        # while k > 0:
        #     mn = float('inf')
        #     ky = -1
        #     for key, val in dic.items():
        #         if val < mn:
        #             mn = val
        #             ky = key            
        #     k -= mn
        #     if k < 0:
        #         break
        #     del dic[ky]
        # return len(dic)


