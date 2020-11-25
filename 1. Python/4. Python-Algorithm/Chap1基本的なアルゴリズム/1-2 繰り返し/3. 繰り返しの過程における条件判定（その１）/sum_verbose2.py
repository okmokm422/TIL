# aからbまでの総和を求める（求める過程の式も表示：その２）
# 繰り返しの回数がnからn-1回に減少 & if文による判定回数がn回から0回に減少

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b): # 最後の値b+1は別にすることで、varbose1の余計な処理実装を修正
    print(f'{i} + ', end='')
    sum += i # sumにiを加える

print(f'{b} = ', end='')
sum += b # sumにbを加える

print(sum)