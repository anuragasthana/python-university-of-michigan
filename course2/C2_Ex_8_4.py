#Use romeo.txt for the file
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l = line.split()
    lst = lst+l
lst.sort()
flst = list()
rlst = range(len(lst))
for a in rlst:
    lst.append("0")
    if lst[a] == lst[a+1]:
        continue
    else:
        flst.append(lst[a])
flst.sort()
print(flst)