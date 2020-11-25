# 記号文字+と-を交互に表示（その１）

print('記号文字+と-を交互に表示します')
n = int(input('全部で何個：'))

for i in range(n): # １からn-1までインクリメント
    if i % 2: # 1(True) = 基数
        print('-', end='')
    else:
        print('+', end='')
print()