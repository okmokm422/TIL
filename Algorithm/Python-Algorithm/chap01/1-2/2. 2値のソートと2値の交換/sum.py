# aからbの総和を求める(for文)

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

# aとbを昇順にソート
# 2値の交換は、次に示す単一の代入文で行うのが定石
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i # sumにiを加える

print(f'{a}から{b}までの総和は{sum}です。')