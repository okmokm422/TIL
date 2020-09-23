print('記号文字*を表示します。')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

for _ in range(n // w):  # 切りがよく改行できる回数
    print('*' * w)

rest = n % w  # 余り
if rest:  # True→0以外
    print('*' * rest)  # 余りの分*をPrint
