# 1から12まで8をスキップして繰り返す（その２）

for i in list(range(1, 8)) + list(range(9, 13)):  # リストを2つ使って記述
    print(i, end=' ')
print()
