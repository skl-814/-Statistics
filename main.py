#!usr/bin/ python3
'''
统计程序 V3.1.1
by skl
https://github.com/
'''

l,ll = [],[]
# code for collecting
while i !="q" or "f":
    i  =input("Number:\n")
    try:
        l.append(float(i))
    except:
        pass
# end
_x = sum(l)/len(l)
    
for a in l:
    ll.append((a-_x)**2)
    
_s = sum(l)/len(ll)
# code for printing...
print(f"平均数：{_x}")
print(f"方差：\n\t{_s}")
print(f"最大值:\n\t{max(l)}")
print(f"最小值:\n\t{min(l)}")
print(f"极差{max(l)-min(l)}")
