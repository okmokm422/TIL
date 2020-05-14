# シーケンスの要素の最大値を表示する
from typing import Any, Sequence

# 関数の定義
def max_of(a: Sequence) -> Any:
    # シーケンスaの要素の最大値を返却する
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

# max_ofがインポートされた際、if文以下が直接が動かないようにする（import文を書いて初めて実行）
if __name__ == '__main__':
    print('配列の最大値を求めます。')
    num = int(input('要素数：'))
    x = [None] * num # 要素数numのリストを生成
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))
        
    print(f'最大値は{max_of(x)}です。')