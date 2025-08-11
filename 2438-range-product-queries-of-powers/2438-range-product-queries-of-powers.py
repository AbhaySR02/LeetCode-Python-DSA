class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        arr = [1]
        for i in range(31):
            if 1 <<i & n:
                arr.append(1 << i)
        for i in range(1, len(arr)):
            arr[i] *= arr[i - 1]
        ans = []
        for a, b in queries:
            ans.append((arr[b + 1] // arr[a]) % MOD)
        return ans