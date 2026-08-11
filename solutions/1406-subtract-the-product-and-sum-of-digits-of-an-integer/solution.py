class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        Sum = 0
        Product = 1

        while temp>0:
            r = temp%10
            temp = temp//10
            Sum = Sum + r
            Product = Product * r

        return (Product - Sum)
