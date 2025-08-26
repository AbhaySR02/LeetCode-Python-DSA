class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total_b_strings=0
        l_count=0
        r_count=0


        for char in s :
            if char == 'L':
                l_count += 1
            elif char == 'R':
                r_count +=1


            if l_count == r_count:
                total_b_strings += 1
                l_count=0
                r_count=0

        return total_b_strings




        