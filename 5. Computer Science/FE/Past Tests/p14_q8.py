from collections import defaultdict

text = 'old king cole was a merry old soul'
# text内の登場回数を格納した辞書word_countを作成
word_count = defaultdict(int)
print(word_count)

for word in text.split():
    word_count[word] += 1
print(word_count)
print(word_count['old'])