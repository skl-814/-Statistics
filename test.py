numlist = [1,2,2,3]
llomg = len(numlist)
setdy = {}
numset =set(numlist)
numset = list(numset)
for da in numset:
    setdy[str(float(da))] = "0"
    for db in numlist:
        if float(da) == float(db):
            ea = setdy[str(float(da))]
            ea = float(ea)
            ea = ea + 1
            ea = str(float(ea))
            setdy[str(da)] = ea

sdy_list = []
for de in setdy.values():
    sdy_list.append(float(de))

    print(float(de))
print()

slmax = max(sdy_list)

print(slmax)
print()
for df,dg in setdy.items():
    if float(dg) == slmax:
        print(f"\n众数：\n{float(df)}")