class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map={}


        for i , num in enumerate(nums):
            compliment= target - num 

            if compliment  in num_map:
                return [num_map[compliment],i]


            num_map[num] = i