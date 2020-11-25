# リストの全要素をenumerate関数で操作（１からカウント）

x = ["John", "George", "Paul", "Ringo"]

for i, name in enumerate(x, 1):
    print(f"x[{i}] = {name}")
