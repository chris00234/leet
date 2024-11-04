class Solution:
    def compressedString(self, word: str) -> str:
        n, l, r=len(word), 0, 0
        ans=[]
        while r<n:
            while r<n and word[r]==word[l]:
                r+=1
            q, rem=divmod(r-l, 9)
            for _ in range(q):
                ans+='9'+word[l]
            if rem>0:
                ans+=chr(rem+ord('0'))+word[l]
            l=r
        return "".join(ans)
        
