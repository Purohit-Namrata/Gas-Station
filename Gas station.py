from typing import List
class Solution:
    def canCompleteCircuit(self,gas:List[int],cost:List[int])->int:
        n=len(gas)
        total_gas=0
        total_cost=0
        current_gas=0
        start_index=0

        for i in range(n):
            total_gas+=gas[i]
            total_cost+=cost[i]
            current_gas+=gas[i]-cost[i]
            
            if current_gas<0:
                start_index=i+1  
                current_gas=0  
        
        if total_gas>=total_cost:
            return start_index 
        else:
            return -1

s=Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # Output: 3
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))              # Output: -1