#very easy solution, go through each sublist and take the sum, if its larger than the max sum so far, then it becomes the max sum

#Feb 24 2022

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        GLOBALMAX = 0
        for i in accounts:
            local_sum = sum(i)
            if local_sum > GLOBALMAX:
                GLOBALMAX = local_sum
        return GLOBALMAX
      
  
