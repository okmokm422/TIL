# prime = {2,3,5,7,13,17}
# fib = {1,1,2,3,4,8,13}
#
# prime_fib = prime | fib
# print(prime_fib)
#
# odd = prime - fib
# print(odd)
#
# A = prime & fib
# print(A)
#
# B = prime ^ fib
# print(B)
#
# codon = ["ATG","GGC","TCC","AAG","TTC","TGG","GAC","TCC"]
# s_codon = set(codon)
# print(len(codon),len(s_codon))
#
# prime = {2,3,5,7,13,17}
# fib = {1,1,2,3,5,8,13}
#
# prime_fib = prime & fib
# if 13 in prime_fib:
#     print("13は素数で、フィボナッチ数である")
# if {2,3} <= prime_fib:
#     print("2,3は素数で、フィボナッチ数でもある")
#
# pref_capitals = {(43.06417,141.34694):"北海道（札幌市）",
#                  (40.82444,140.74):"青森県（青森市）",
#                  (39.70361,141.1525):"岩手県（盛岡市）"
#                  }
# loc = (39.70361,141.1525)
# for K in pref_capitals:
#     if K == loc:
#         print(pref_capitals[K])
#         break

# loc = (41.768793,140.72881)
# nearest_cap = ""
# nearest_dist = 10000
# for key in pref_capitals:
#     dist = (loc[0] - key[0])**2 + (loc[1] - key[1])**2
#     if nearest_dist > dist:
#         nearest_dist = dist
#         nearest_cap = pref_capitals[key]
# print(nearest_dist,nearest_cap)
#
# cnt = 1
# while cnt <= 100:
#     if cnt % 3 == 0 and cnt % 5 == 0:
#         print("Fizzbuzz")
#     elif cnt % 3 == 0:
#         print("Fizz")
#     elif cnt % 5 == 0:
#         print("Buzz")
#     else:
#         print(cnt)
#     cnt = cnt + 1
#
# from random import randint
# hands = {0:"グー",1:"チョキ",2:"パー"}
# rules = {(0,0):"あいこ",(0,1):"勝ち",(0,2):"負け",
#          (1,0):"負け",(1,1):"あいこ",(1,2):"勝ち",
#          (2,0):"勝ち",(2,1):"負け",(2,2):"あいこ"}
# while True:
#     pc_hand = randint(0,2)
#     user_hand_str = input("0:グー、1:チョキ、2:パー、3：やめる")
#     if user_hand_str == "3":
#         break
#     if user_hand_str not in ("0","1","2"):
#         continue
#     user_hand = int(user_hand_str)
#     print("あなた"+hands[user_hand]+"、コンピュータ"+hands[pc_hand])
#     print(rules[(user_hand,pc_hand)])


# a_num = 59
# for num in range (2,a_num):
#     if a_num % num == 0:
#         print(a_num, "は素数ではありません")
#         break
# else:
#     print(a_num, "は素数です")

# def fizzbuzz(count=100, fizzmod=3, buzzmod=5):
#     for cnt in range(1,count+1):
#         if cnt%fizzmod == 0 and cnt%buzzmod ==0:
#             print("Fizzbuzz")
#         elif cnt%fizzmod == 0:
#             print("Fizz")
#         elif cnt%buzzmod == 0:
#             print("Buzz")
#         else:
#             print(cnt)
# fizzbuzz(20)
#
# local_var = 1
# def test_func(an_arg):
#     local_var = an_arg
#     print("test_func()の中 =" , local_var)
# test_func(200)
# print("test_func()の外 =",local_var)
#
# import matplotlib
# import matplotlib.pyplot as plt
#
# str_speeds = "38 42 20 40 39"
# str_armor = "80 50 17 50 51"
# speeds = str_speeds.split(" ")
# amors = str_armor.split(" ")
# markers = [ "o", "v", "^", "<", ">"]
# for idx in range(len(speeds)):
#     x = int(speeds[idx])
#     y = int(amors[idx])
#     plt.scatter(x,y,marker=markers[idx])
#     plt.xlim(0,100)
#     plt.ylim(0,100)
# plt.show()
# ↑for文の中だとループ対象に！





