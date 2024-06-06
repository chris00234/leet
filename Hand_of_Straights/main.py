class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        dict_ ={}

        for num in hand:
            dict_[num] = dict_.get(num, 0) + 1
        
        print(min(dict_))
        while dict_:
            min_ = min(dict_)
            dict_[min_] -= 1
            if dict_[min_] == 0:
                del dict_[min_]
            for i in range(groupSize - 1):
                if (min_ + 1) in dict_:
                    dict_[min_ + 1] -= 1
                    if dict_[min_ + 1] == 0:
                        del dict_[min_ + 1]
                    min_ = min_ + 1
                else:
                    return False
        return True
