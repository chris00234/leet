class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for _ in ratings]
        # if ratings[1] < ratings[0]:
        #     candy[0] = 2
        # if ratings[-1] > ratings[-2]:
        #     candy[-1] = 2

        for i in range(len(ratings) -2, -1, -1):
            curr = ratings[i]
            if curr > ratings[i + 1]:
                candy[i] = candy[i + 1] + 1
        
        for i in range( 1, len(ratings)):
            curr = ratings[i]
            if curr > ratings[i - 1]:
                candy[i] = candy[i -1] + 1

        for i in range( 1, len(ratings) - 1):
            curr = ratings[i]
            #greater than two neighbors
            if curr > ratings[i - 1] and curr > ratings[i + 1]:
                if candy[i - 1]>= candy[i + 1]:
                    candy[i] = candy[i - 1] + 1
                else:
                    candy[i] = candy[i + 1] + 1
            #ascending order
            if curr > ratings[i - 1] and curr <= ratings[i + 1]:
                candy[i] = candy[i - 1] + 1
            
            #descending order
            if curr <= ratings[i - 1] and curr > ratings[i + 1]:
                candy[i] = candy[i + 1] + 1
        print(candy)
        return sum(candy)

# 3 1 5 5 5 6 7 2 2 3 1 2 6
# 2 1 2 1 2 3 4 1 1 1 1 1 2

# 3 1 5 4 5 6 7 2 1 3 4 5 2
# 2 1 3 1 2 2 3 2 1 2 2 3 1

# 3 1 5 4 5 6 7 2 1 3 4 5 2
# 2 1 2 1 2 3 4 2 1 2 3 4 1

# 3 1 5 4 5 6 7 2 1 3 4 5 2
# 1 1 3 1 2 2 3 2 1 2 2 3 1