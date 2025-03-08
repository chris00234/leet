class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        block_list = []
        for i in range(len(blocks)):
            if blocks[i] == "W":
                block_list.append(1)
            else:
                block_list.append(0)
        mn = 100
        while r <= len(block_list):
            mn = min(mn, sum(block_list[l:r]))
            l += 1
            r += 1
        return mn
