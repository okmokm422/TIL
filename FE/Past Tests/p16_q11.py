from collections import  defaultdict
heights = { ('男', 165), ('女', 155), ('男', 170), ('女', 160), ('男',167), 
            ('女', 152), ('男', 180), ('女', 148), ('男', 172), ('女', 159)}

heights_by_sex = defaultdict(list)
for sex, height in heights:
    heights_by_sex[sex].append(height)

average_height = {
    sex: sum(hlist) / len(hlist)
    for sex, hlist in heights_by_sex.items()
}

for sex, avg in average_height.items():
    print(sex, avg)