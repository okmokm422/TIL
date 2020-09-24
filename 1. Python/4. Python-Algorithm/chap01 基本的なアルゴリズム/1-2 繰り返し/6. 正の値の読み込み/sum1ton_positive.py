# 1からnまでの総和を求める（nに正の整数値読み込む）

print('1からnまでの総和を求めます')

while True:
    n = int(input('nの値：'))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i  # sumにiを加える
    i += 1 * i  # iに1を加える
print(f'1から{n}までの総和は{sum}です。')


'''
Python : 前判定繰り返し
前判定繰り返し文(while or for) とbreakを組み合わせる
'''
