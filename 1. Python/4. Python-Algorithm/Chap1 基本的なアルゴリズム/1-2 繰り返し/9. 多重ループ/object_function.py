# 関数内外で定義された変数とオブジェクト
# オブジェクトと変数の識別番号を表示

n = 1  # 広域変数（関数内外で利用できる）

def put_id():
    x = 1  # 局所変数（関数内でのみ利用できる）
    print(f'id(x) = {id(x)}')


print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()
