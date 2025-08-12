class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        candidates = []
        num = 1
        while num ** x <= n:
            candidates.append(num ** x)
            num += 1

        memo = {}

        def solve(index, target):
          
            if target == 0:
                return 1

            if target < 0 or index >= len(candidates):
                return 0

        
            if (index, target) in memo:
                return memo[(index, target)]

           
            ways_if_used = solve(index + 1, target - candidates[index])
   
            ways_if_not_used = solve(index + 1, target)
            
       
            total_ways = ways_if_used + ways_if_not_used
           
            memo[(index, target)] = total_ways
            return total_ways

        MOD = 10**9 + 7
        return solve(0, n) % MOD