class Solution:
    def buyTwoChocolates(self, prices: list[int], money: int) -> int:
        
        cheapest = 101
        second_cheapest = 101
        
        for price in prices:
            if price < cheapest:
                second_cheapest = cheapest
                cheapest = price
            elif price < second_cheapest:
                second_cheapest = price

        min_cost = cheapest + second_cheapest
        
        if min_cost <= money:
            return money - min_cost
        else:
            return money