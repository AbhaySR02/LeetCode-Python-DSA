class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Determines if there are two distinct indices i and j in the array such that
        nums[i] == nums[j] and abs(i - j) <= k.

        The optimal solution uses a hash map to store the most recent index of
        each number encountered. This allows for a single pass through the array.

        Time Complexity: O(n)
        Space Complexity: O(n) in the worst case.
        """
        
        # Initialize a hash map to store the last seen index of each number.
        # Key: number, Value: index
        seen_map = {}
        
        # Iterate through the list with both the index and the number.
        for index, num in enumerate(nums):
            # Check if we have seen this number before.
            if num in seen_map:
                # If we have, get its previous index.
                previous_index = seen_map[num]
                
                # Check if the distance between the current and previous index is within k.
                if index - previous_index <= k:
                    # If it is, we have found our pair. Return True.
                    return True
            
            # Whether we found a pair or not, we must update the map with the
            # most recent index for this number.
            seen_map[num] = index
            
        # If the loop completes without finding any such pair, return False.
        return False

