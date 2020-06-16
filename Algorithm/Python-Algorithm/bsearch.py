from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    # シーケンスaからkeyと一致する要素を二分探索
    pl = 0 # 先頭の添字
    pr = len(a) - 1 # 末尾の添字

    while True:
        pc = (pl + pr) // 2 # 中央要素の添字
        if a[pc] == key:
            return pc # 探索成功
        elif a[pc] < key: # keyが中央要素より後半にあるとき
            pl = pc + 1 # 探索範囲を後半に絞り込む。先頭の添字を前回の中央要素+1に。
        else: # keyが中央要素より前半にあるとき
            pr = pc - 1 # 対象範囲を前半に絞り込む。末尾の添字を前回の中央要素-1に。
        if pl > pr:
            break
    return -1

if __name__ == "__main__":
    num = int(input('要素数：'))
    x = [None] * num # 要素数numの配列を作成

    print('昇順に入力してください。')

    x[0] = int(input('x[0]：'))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= x[i-1]:
                break

    ky = int(input('探す値：')) # キーkyの読込み

    idx = bin_search(x, ky) # kyと等価な要素をxから探索

    if idx == -1:
        print('その値の要素は存在しません。')
    else:
        print(f'その値はx[{idx}]にあります。')