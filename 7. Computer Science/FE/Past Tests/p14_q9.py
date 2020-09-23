record = [ ('吉田太郎', 2000), ('斎藤一', 1750), ('岸本美登利里', 2810) ]
record.sort(key=lambda x: x[1], reverse=True)
print('今月の成績')
for name, score in record:
    print(name[:2] + ':', 'X' * (score // 100))