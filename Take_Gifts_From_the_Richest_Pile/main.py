class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            mx = max(gifts)
            idx = gifts.index(mx)
            sq = math.floor(math.sqrt(mx))
            gifts[idx] = sq
        return sum(gifts)
