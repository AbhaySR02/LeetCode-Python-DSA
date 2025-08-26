class Solution:
    def reverse(self, x: int) -> int:
        rev_n=0

        sign=1
        if x<0:
            sign= -1
            x= abs(x)

        while x!=0:
            last_digit = x%10

            if rev_n > 214748364 or (rev_n == 214748364 and last_digit > 7):
                return 0

            rev_n= rev_n*10 + last_digit 
            x = x//10

        return rev_n * sign
