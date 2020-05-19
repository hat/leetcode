"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns
the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive
days (starting from today and going backwards) for which the price of the stock was
less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
"""

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.length = -1
        

    def next(self, price: int) -> int:
        size = self.length
        if size == -1:
            self.prices.append((price, 1))
            self.length += 1
        else:
            cur_count = 1
            i = size
            while i >= 0 and self.prices[i][0] <= price:
                cur_count += self.prices[i][1]
                self.prices.pop(i)
                self.length -= 1
                i -= 1
            self.prices.append((price, cur_count))

            self.length += 1
        return self.prices[self.length][1]


class TestSolution:

    def setup(self):
        self.answer = StockSpanner()

    def test_one(self):
        assert self.answer.next(100) == 1
        assert self.answer.next(80) == 1
        assert self.answer.next(60) == 1
        assert self.answer.next(70) == 2
        assert self.answer.next(60) == 1
        assert self.answer.next(75) == 4
        assert self.answer.next(85) == 6