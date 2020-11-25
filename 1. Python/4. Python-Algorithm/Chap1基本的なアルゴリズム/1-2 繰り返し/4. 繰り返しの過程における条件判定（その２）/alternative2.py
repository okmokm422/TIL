# 記号文字+と-を交互に表示（その２）

print('記号文字+と-を交互に表示します。')
n = int(input('全部で何個：'))

for _ in range(n // 2): # ２で割り切れる分だけ+-を改行なしprint
    print('+-', end='') 
if n % 2: # ２で割り切れなかった分、最後に+をprint
    print('+', end='')
print()