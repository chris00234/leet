class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ret = []
        for r in range(len(matrix)):
            mn = min(matrix[r])
            print(mn)
            for c in range(len(matrix[0])):
                if matrix[r][c] != mn:
                    continue
                else:
                    find_max = True
                    for tmp in range(len(matrix)):
                        if matrix[tmp][c] > mn:
                            find_max = False
                            break
                    if find_max:
                        ret.append(mn) 
        return ret

                
