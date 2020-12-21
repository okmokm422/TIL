# オープンアドレス法によるハッシュ

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# バケットの属性


class Status(Enum):
    OCCUPIED = 0  # データ格納
    EMPTY = 1  # 空
    DELETED = 2  # 削除済


class Bucket:
    """ハッシュを構成するバケット"""

    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        """初期化"""
        self.key = key  # キー
        self.value = value  # 値
        self.stat = stat  # 属性

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """全フィールドに値を設定"""
        self.key = key  # キー
        self.value = value  # 値
        self.stat = stat  # 属性

    def set_status(self, stat: Status) -> None:
        """属性を設定"""
        self.stat = stat


class OpenHash:
    """オープンアドレス法を実現するハッシュクラス"""

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity  # ハッシュ法の容量
        self.table = [Bucket()] * self.capacity  # ハッシュ表

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        # keyがint型でないとき : md5アルゴリズムによるhash値をhashとする
        """
        hashlib.md5() : hash値を生成
        str(key).encode() : 文字列にしてbyte文字列を生成
        hexdigest() : ハッシュ値を16進数の文字列で取り出す
        int( , 16) : 16進数の文字列をint型に変換
        """
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """最ハッシュ値を求める"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """キーがkeyであるバケットの探索"""
        hash = self.hash_value(key)  # 探索するキーのハッシュ値
        p = self.table[hash]  # 着目バケット

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.table[hash]
        return None
