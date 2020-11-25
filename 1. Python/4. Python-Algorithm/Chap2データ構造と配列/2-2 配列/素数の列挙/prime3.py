# 1000以下の素数を列挙

counter = 0  # 乗除算の回数
ptr = 0  # 　素数の個数
prime = [None] * 500  # 素数を格納

prime[ptr] = 2  # 2は素数である
ptr += 1
prime[ptr] = 3  # 3は素数である
ptr += 1

for n in range(5, 1001, 2):  # 対象は奇数
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f"乗除算を行った回数：{counter}")
