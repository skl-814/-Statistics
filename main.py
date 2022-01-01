#!usr/bin/var python3
#maker:SKL
import json

num = " "
numlist = []

print("输入数据（回车完成)")
while num != "":
    num = input("\n数据:\n")
    if num == "":
        break
    else:
        try:
            num = float(num)
        except:
            print("Wrong!")
            while True:
                print("",end="")
        else:
            numlist.append(num)

numlist.sort()

llong = len(numlist)

a = 0
for aa in numlist:
    a = a + aa

a = a/llong
print(f"\n\n平均数：\n{a}")
d1 = str(a)

aaa = 0
for aa in numlist:
    ab = aa - a
    ab = ab ** 2
    aaa = aaa + ab

f_num = aaa/llong
print(f"\n方差：\n{f_num}")
d2 = str(f_num)

print("\n最小值:\n",min(numlist))
d3 = str(min(numlist))
print("\n最大值:\n",max(numlist))
d4 = str(max(numlist))
ccc = max(numlist)-min(numlist)
print("\n极差:\n",ccc)
d5 = str(ccc)
del ccc
numlist.sort()
if llong%2 == 0:
    c1 = int(llong / 2 - 1)
    c2 = int(c1 + 1)

    c1 = numlist[c1]
    c2 = numlist[c2]
    c3 = (c1 + c2) / 2
    print("\n中位数：\n",c3)
    d6 = str(c3)
elif llong%2 != 0:
    c1 = int(llong / 2 + 0.5 - 1)
    c1 = numlist[c1]
    print("\n中位数：\n",c1)
    d6 = str(c1)


#with open("history.json","a",) as hf:
#    json.dump(numlist,hf)
#    json.dump(d1,hf)
#    json.dump(d2,hf)
#    json.dump(d3,hf)
#    json.dump(d4,hf)
#    json.dump(d5,hf)
#    json.dump(d6,hf)
#    json.dump("____________________",hf)

with open("history.txt","a") as hft:
    hft.write(str(numlist)+"\n")
    hft.write(d1+"\n")
    hft.write(d2+"\n")
    hft.write(d3+"\n")
    hft.write(d4+"\n")
    hft.write(d5+"\n")
    hft.write(d6+"\n")
    hft.write("\n")
    hft.write("____________________")
    hft.write("____________________")
    hft.write("____________________")
    hft.write("___________________")
    hft.write("\n")
    hft.write("\n")

while True:
    print("",end="")

#     SKL make