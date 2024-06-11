class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict_1 = {}

        for i in arr1:
            dict_1[i] = dict_1.get(i, 0) + 1
        
        ret = []
        for i in arr2:
            if i in dict_1:
                for j in range(dict_1[i]):
                    ret.append(i)
                del dict_1[i]
        if len(dict_1) == 0:
            return ret
        con = []
        for key in dict_1:
            for j in range(dict_1[key]):
                con.append(key)
        con.sort()
        ret.extend(con)
        return ret
