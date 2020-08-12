# aからbまでの総和を求める（求める過程の式も表示）
# else文1回の判定のために、if文の判定がn回行われるため、不適切な実装。

print('aからｂまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

# a~bの順番の昇順に並び替え
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b: # 途中の式の表示（数値 + 数値 + 数値 + ...）
        print(f'{i} + ', end='')
    else: # 最後
        print(f'{i} = ', end='')
    sum += i # sumにiを加える

print(sum)