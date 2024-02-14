class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        init = 0
        diff = 0
        count = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            diff += gas[i] - cost[i]

            if diff < 0:
                diff = 0
                init = i + 1
        
        return -1 if total_gas < total_cost else init


            
                
