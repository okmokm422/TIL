from random import random

monk_fish_team = [158,157,163,157,145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total/length
variance = 0

for height in monk_fish_team:
    variance += (height-mean)**2

variance = variance/length #標準偏差
#print(variance)

v = variance**0.5 #標準偏差
#print(v)

#複利計算
savings = 100
for i in range(15):
    savings += savings * 0.05
#print(savings)

#年齢計算
a_year = 2080
if a_year >= 1993:
    if a_year == 1993:
        print(a_year,"年、れに誕生")
    else:
        print(a_year,"れに誕生",a_year-1993,"歳")

#素数計算
a_num = 4
for num in range(2,a_num):
    if a_num % num == 0:
        print(a_num,"は素数ではありません")
        break

#input("好きな数字は？")

import random
print(random.random())
print(random.randint(0,6))
a_list = [0,1,2,3,4,5]
random.shuffle(a_list)
print(a_list)
print(random.choice)

from statistics import median
monk_fish_team = [158,157,163,157,145]
volleyball_team = [143,167,170,165]
print(median(monk_fish_team))
print(median(volleyball_team))