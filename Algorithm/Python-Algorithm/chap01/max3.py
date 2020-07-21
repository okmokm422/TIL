# ３つの整数値を読み込んで最大値を求めて表示

print('三つの整数の最大値を求めます')

a = int(input('整数aの値：'))
b = int(input('整数bの値：'))
c = int(input('整数cの値：'))

maximun = a
if b > maximun: maximun = b
if c > maximun: maximun = c

print(f'最大値は{maximun}です。')