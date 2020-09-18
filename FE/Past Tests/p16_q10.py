import re
table = [('みかん', 'ミカン'), ('りんご', 'リンゴ'), ('ぶどう', 'ブドウ')]

f = open('sample.txt', 'r', encoding='utf-8')

for line in f:
    for str1, str2 in table:
        line = re.sub(str1, str2, line)
    print(line, end="")

f.close()
