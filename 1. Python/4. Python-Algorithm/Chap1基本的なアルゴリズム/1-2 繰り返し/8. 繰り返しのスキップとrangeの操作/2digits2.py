# ２つの正の整数値（10~99）を読み込む

print('２つの整数値を入力してください。')

while True:
    no = int(input('値は：'))
    if 10 <= no <= 99:
        break
print(f'読み込んだのは{no}です。')
