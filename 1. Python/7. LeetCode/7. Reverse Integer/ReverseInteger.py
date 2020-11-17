class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:  # positive
            a = int(str(x)[::-1])  # x:positive=>str=>sort=>int
        if x <= 0:  # x:negative=>-x:positivestr=>sort=>int
            a = -1 * int(str(x*-1)[::-1])
        mina = -2 ** 31  # 下限
        maxa = 2 ** 31 - 1  # 上限
        if a not in range(mina, maxa):
            return 0
        else:
            return a
