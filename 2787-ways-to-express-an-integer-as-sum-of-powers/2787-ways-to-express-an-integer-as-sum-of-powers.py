class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        # --- Step 1: Generate the "Building Blocks" ---
        candidates = []
        num = 1
        while num ** x <= n:
            candidates.append(num ** x)
            num += 1
        
        # --- Step 2: Bottom-Up Dynamic Programming ---
        # dp[i] will store the number of ways to make the sum 'i'.
        # The size is n+1 to accommodate sums from 0 to n.
        dp = [0] * (n + 1)
        
        # Base Case: There is exactly one way to make a sum of 0 (by choosing no numbers).
        dp[0] = 1
        
        MOD = 10**9 + 7

        # Iterate through each building block (candidate number).
        for cand in candidates:
            for j in range(n, cand - 1, -1):
                dp[j] = (dp[j] + dp[j - cand]) % MOD
        
        # The final answer is the number of ways to make the sum 'n'.
        return dp[n]
