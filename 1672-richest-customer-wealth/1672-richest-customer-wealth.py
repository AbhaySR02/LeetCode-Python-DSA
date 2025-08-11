class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(customer_accounts) for customer_accounts in accounts)