# ｎ個の記号文字*個ごとに開業しながら表示（その１）

print('記号文字*を表示します。')
n = int(iput('全部で何個：'))
w = int(input('何個ごとに改行：'))

for i in range(n):  # ０からn-1回*をprint
    print('*', end='')
    if i % w == w - 1:
        print(end='')
