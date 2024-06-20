class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position=sorted(position)
        l,r=1,max(position)
        ans=1
        def canPlaceBall(mid,position,m):
            place=position[0]+mid
            m-=1
            for i in range(1,len(position)):
                if position[i]>=place:
                    m-=1
                    place=position[i]+mid  
                if m==0:
                    return True                 
            return False            

        while l<=r:
            mid=(l+r)//2
            if canPlaceBall(mid,position,m):
                l=mid+1
                ans=max(ans,mid)
            else:
                r=mid-1
        return ans            

