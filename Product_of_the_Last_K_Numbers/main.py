class ProductOfNumbers:

    def __init__(self):
        self.li = []
        

    def add(self, num: int) -> None:
        self.li.append(num)

    def getProduct(self, k: int) -> int:
        l = len(self.li)
        return math.prod(self.li[-1 * k :])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
