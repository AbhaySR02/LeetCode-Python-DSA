class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_counts={}

        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1


        total_pairs=0
        for count in num_counts.values():
            total_pairs += count* (count-1)//2


        return total_pairs




        