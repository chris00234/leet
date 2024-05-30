class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d=0
        for i in range(len(arr)):
            c=arr[i]
            for j in range(i+1,len(arr)):
                c^=arr[j]
                if c==0:
                    d+=j-i
        return d
