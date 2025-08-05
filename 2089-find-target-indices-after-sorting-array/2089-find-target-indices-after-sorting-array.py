class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_count=sum(1 for num in nums if num<target)
        target_count=nums.count(target) 

        return list (range(smaller_count,smaller_count+target_count))
        return