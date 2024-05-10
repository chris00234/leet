class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []
        dict_ = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fraction.append(arr[i]/arr[j])
                dict_[arr[i]/arr[j]] = [arr[i], arr[j]]
        
        sorted_fraction = sorted(fraction, key=lambda x: x)
        # print(sorted_fraction)
        return dict_[sorted_fraction[k - 1]] if len(arr) > 2 else arr
