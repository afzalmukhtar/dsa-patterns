class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        # We store (price, count) in the stack.
        # price: the stock price for that day
        # count: the total number of consecutive days with price <= current day's price
        #
        # When we pop an element from the stack, we add its count to our current count.
        # This is because the popped element already "absorbed" all the days before it
        # that were smaller or equal. By storing the span (count), we avoid having
        # to look backward multiple times.
        while self.stack and price >= self.stack[-1][0]:
            _, span = self.stack.pop()
            count += span
            
        self.stack.append((price, count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
