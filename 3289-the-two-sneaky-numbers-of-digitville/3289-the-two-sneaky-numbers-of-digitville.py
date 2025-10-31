class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        sum_ = sum(nums)
        squared_sum = sum(x * x for x in nums)
        sum2 = sum_ - n * (n - 1) // 2
        squared_sum2 = squared_sum - n * (n - 1) * (2 * n - 1) // 6
        x1 = (sum2 - math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        x2 = (sum2 + math.sqrt(2 * squared_sum2 - sum2 * sum2)) / 2
        return [int(x1), int(x2)]