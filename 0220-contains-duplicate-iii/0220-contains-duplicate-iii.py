from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window=SortedList()
        for i in range(len(nums)):
            index=window.bisect_left(nums[i]-valueDiff)
            if index<len(window) and abs(window[index]-nums[i])<=valueDiff:
                return True
            window.add(nums[i])
            if i>=indexDiff:
                window.remove(nums[i-indexDiff])
        return False


        
        



