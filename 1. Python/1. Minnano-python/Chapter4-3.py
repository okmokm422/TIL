orig_str = "いっぱい"
orig_str.replace("い", "お")
print(orig_str)

str_num = "1,000,000"
num = str_num.replace(",", "")
print(num)

import matplotlib.pyplot as plt

str_speeds = "38 42 20 40 39"
str_armor = "80 50 17 50 51"
speeds = str_speeds.split(" ")
armors = str_armor.split(" ")
markers = ["o", "v", "^", "<", ">"]

for idx in range(len(speeds)):
    x = int(speeds[idx])
    y = int(armors[idx])
    plt.scatter(x,y,marker=markers[idx])
# plt.show()

str_speeds = "38 42 20 40 39"
speeds = str_speeds.split()
print(speeds)
csep_speeds = ",".join(speeds)
print(csep_speeds)

str_speeds2 = "38    42 20 40 39"
s = str_speeds2.replace(" ", ",")
print(s)

str_speeds2 = "38    42 20 40 39"
speeds2 = str_speeds2.split()
print(speeds2)
csep_speeds = ",".join(speeds2)
print(csep_speeds)

def func():
    words = """ゆく河の流れは絶えずして
しかももとの水にあらず"""
    print(words)
func()

def func():
    words = "ゆく河の流れは絶えずして\nしかももとの水にあらず"
    print(words)
func()

linkstr = "<a href='{}'>{}</a>"
for i in ["http://python.org",
          "http://pypy.org",
          "http://cyhton.org"]:
    print(linkstr.format(i,i.replace("http://", "")))

a = "{0},{1},{0}".format("spam","ham")
print(a)

b = "{food1} {food2} {food1}".format(food1="spam",food2="ham")
print(b)

d = {"name":"Guido","birthyear":1964}
print("{0[birthyear]} is {0[name]}'s birthyear.".format(d))

import sys
print("Python version:{0.version}".format(sys))

name = "you"
print(f"まずは{name}が落ち着け")


