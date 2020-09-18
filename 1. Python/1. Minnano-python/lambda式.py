tank_data = [("Ⅵ号戦車", 38, 80, 75),("LT-38", 42, 50, 37),
             ("八九式中戦車", 20, 17, 57),("Ⅲ号突撃砲", 40, 50, 75),
             ("M3中戦車", 39, 51, 75)]

# def evaliate_tankdata(tup):
#     return tup[1]+tup[2]+tup[3]

tank_data.sort(key=lambda tup: sum(tup[1:4],reverse=True))
print(tank_data)
