# チェイン法によるハッシュ

# 同一ハッシュ値をもつデータをチェイン状に線形リストでつなぐ方法

from __future__ import annotations
from typing import Any, Type
import hashlib


# 個々のバケット（ハッシュ表の各要素）を表す
class Node:
    """ハッシュを構成するノード"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """初期化"""
        self.key = key  # キー
        self.value = value  # 値
        self.next = next  # 後続ノードへの参照


class ChainedHash:
    """チェイン法を実現するハッシュクラス"""

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity  # ハッシュ表の容量
        self.table = [None] * self.capacity  # 同じハッシュ値を指す線形リスト

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        # keyがint型のとき : key%capacityがhash値
        if isinstance(key, int):
            return key % self.capacity
        # keyがint型でないとき : hash256アルゴリズムによるhash値をhashとする
        """
        hashlib.sha256() : hash値を生成
        str(key).encode() : 文字列にしてbyte文字列を生成
        hexdigest() : ハッシュ値を16進数の文字列で取り出す
        int( , 16) : 16進数の文字列をint型に変換
        """
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """キーkeyを持つ要素の探索（値を返却）"""
        hash = self.hash_value(key)  # 探索するキーのハッシュ値
        p = self.table[hash]  # 着目ノード

        while p is not None:
            if p.key == key:
                return p.value  # 探索成功
            p = p.next  # 後続ノードに着目

        return None  # 探索失敗

    def add(self, key: Any, value: Any) -> bool:
        """キーがkeyで値がvalueの要素の追加"""
        hash = self.hash_value(key)  # 追加するキーのハッシュ値
        p = self.table[hash]  # 着目ノード

        while p is not None:
            if p.key == key:
                return False  # 追加失敗
            p = p.next  # 後続ノードに着目

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # ノードを挿入
        return True

    def remove(self, key: Any) -> bool:
        """キーkeyをもつ要素の削除"""
        hash = self.hash_value(key)  # 削除するキーのハッシュ値
        p = self.table[hash]  # 着目ノード
        pp = None  # 前回の着目ノード

        while p is not None:
            if p.key == key:  # キーを見つけたら
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next  # 後続ノードに着目
        return False

    def dump(self) -> None:
        """ハッシュ表をダンプ（表示する）"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'   → {p.key}({p.value})', end='')
                p = p.next
            print()
