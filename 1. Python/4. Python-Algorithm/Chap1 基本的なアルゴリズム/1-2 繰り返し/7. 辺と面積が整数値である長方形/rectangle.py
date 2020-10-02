# 縦横が整数で面積がareaの長方形の辺の長さを列挙
# →　約数の列挙

area = int(input('面積は：'))

for i in range(1, area + 1):
    if i * i > area:  # iが短編の間はループする
        break
    if area % i:  # 割り切れない
        continue  # ループ本体の後続部をスキップ
    print(f'{i}×{area // i}')
