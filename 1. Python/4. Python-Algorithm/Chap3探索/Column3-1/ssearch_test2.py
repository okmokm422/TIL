# 線形探索を行う関数seq_searchの利用例（その2）

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}の中の5.6の添字は{seq_search(t, 5.6)}です。')
print(f'{s}の中の"n"の添字は{seq_search(s, "n")}です。')
print(f'{a}の中の"DTS"の添字は{seq_search(a, "DTS")}です。')
