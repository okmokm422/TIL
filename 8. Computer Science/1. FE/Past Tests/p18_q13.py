from collections import  defaultdict
total = defaultdict(int)
try:
    with open('uriage.txt', 'r', encoding='utf-8') as f:
        for line in f:
            item, num, price = line.split(',')
            total[item] += int(price) * int(num)
    for item, sum in total.items():
        print(item + ':', sum)
except FileNotFoundError:
    print('ファイルが見つかりません')