class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit = [0 for i in range(24)]
        for num in candidates:
            bin_str = str(bin(num))
            bin_str = bin_str[2:]
            bin_str = bin_str[::-1]
            for i in range(len(bin_str)):
                if bin_str[i] == '1':
                    bit[i] += 1
        return max(bit)

        
