class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determines if a number is a power of four using a bitwise trick.
        
        A number n is a power of four if and only if:
        1. It is positive.
        2. It is a power of two (has only one '1' bit in its binary representation).
        3. That single '1' bit is in an even-numbered position (0, 2, 4, ...).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        # Check 1: Must be positive.
        is_positive = n > 0
        
        # Check 2: Must be a power of two (only one '1' bit).
        is_power_of_two = (n & (n - 1)) == 0
        
        # Check 3: The '1' bit must be in an even-numbered position.
        # The mask 0x55555555 in binary is ...01010101, which has 1s in all
        # the even-numbered bit positions (0, 2, 4, etc.).
        # If (n & mask) is not zero, it means the '1' in n lined up with a '1' in the mask.
        is_one_in_even_spot = (n & 0x55555555) != 0
        
        return is_positive and is_power_of_two and is_one_in_even_spot


        