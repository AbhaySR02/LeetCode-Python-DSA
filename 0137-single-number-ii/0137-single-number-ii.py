class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        # We can use a list to store the sum of bits for each position
        bit_sums = [0] * 32

        # Step 1: Count the bits for each position
        for num in nums:
            for i in range(32):
                # We check the i-th bit of num
                if (num >> i) & 1:
                    bit_sums[i] += 1

        # Step 2: Reconstruct the final number
        result = 0
        for i in range(32):
            # The remainder modulo 3 determines the bit of the single number
            if bit_sums[i] % 3 == 1:
                # Set the i-th bit of the result to 1
                result |= (1 << i)

        # Step 3: Handle the negative sign for 32-bit integers
        # If the 31st bit (the sign bit) of the original result is 1,
        # it means the number is negative. We need to convert it back to a negative number.
        if (result >> 31) & 1:
            result = result - (1 << 32)
        
        return result