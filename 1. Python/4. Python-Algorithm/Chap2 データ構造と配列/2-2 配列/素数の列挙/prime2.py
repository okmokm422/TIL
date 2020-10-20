# 1000以下の素数を列挙（第２版）

counter = 0  # 除算の回数
ptr = 0  # 得られた素数の個数
prime = None * 500  # 素数を格納する配列

prime[ptr] = 2  # 2は素数である
ptr += 1

for n in range(3, 1001, 2):  # 対象は奇数
    for i in range(1, ptr):  # 既に得られた素数で割ってみる
        counter += 1
        if n % prime[i] == 0:  # 割り切れると素数ではない
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f"除算を行った回数：{counter}")
