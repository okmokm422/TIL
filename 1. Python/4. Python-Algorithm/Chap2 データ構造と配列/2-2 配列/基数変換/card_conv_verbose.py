# 詠み込んだ10進数を2進数〜36進数へと基数変換して表示

def card_conv(x: int, r: int) -> str:
    """整数値xをr進数に変換した数値を表す文字列を返却"""

    d = ''  # 変換後の文字列
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ'
    n = len(str(x))  # 変換前の桁数

    print(f"{r:2} | {x:{n}d}")
    while x > 0:
        print("   +" + (n + 2) * "-")
        if x // r:
            print(f"{r:2} | {x // r:{n}d} ･･･ {x % r}")
        else:
            print(f"     { x // r:{n}d} ･･･ {x % r}")

        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == "__main__":
    print("10進数を基数変換します。")

    while True:
        while True:  # 非負の整数値を読み込む
            no = int(input("変換する非負の整数："))
            if no > 0:
                break

        while True:  # 2~36の整数値を読み込む
            cd = int(input("何進数に変換しますか（2-36）："))
            if 2 <= cd <= 36:
                break

        print(f"{cd}進数では{card_conv(no, cd)}です。")

        retry = input("もう一度しますか（Y･･･はい／N･･･いいえ）")
        if retry in {"N", "n"}:
            break
