class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determines if an integer is a power of three using a mathematical trick.

        The largest power of 3 that fits within a 32-bit signed integer is 3^19.
        A number n is a power of three if and only if it is a positive number
        that evenly divides this largest power of three.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        # The logic combines two checks:
        # 1. n > 0: A power of three must be positive.
        # 2. 1162261467 % n == 0: The largest integer power of 3 must be
        #    divisible by n if n itself is a power of 3.
        
        return n > 0 and 1162261467 % n == 0

