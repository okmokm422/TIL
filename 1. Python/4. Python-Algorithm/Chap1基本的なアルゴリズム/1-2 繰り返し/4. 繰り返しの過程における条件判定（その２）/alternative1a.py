# 記号文字+と-を交互に表示（その1-a）

print('記号文字+と-を交互に表示します')
n = int(input('全部で何個：'))

for i in range(1, n + 1):
    if i % 2: # 1 = True = 基数
        print('+', end='')
    else: # 偶数
        print('-', end='')
