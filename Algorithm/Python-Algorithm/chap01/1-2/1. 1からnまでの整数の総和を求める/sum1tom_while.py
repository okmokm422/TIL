# 1からnまでの総和を求める（while文）

print('1からnまでの総和を求めます。')
n = int(input('ｎの値：'))

sum = 0
i = 1

while i <= n: # iがn以下のあいだ繰り返す
    sum += i # sumにiを加える
    i += 1 # iに1を加える
print(f'1から{n}までの総和は{sum}です。')