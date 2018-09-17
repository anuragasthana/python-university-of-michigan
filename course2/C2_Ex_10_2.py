#Use mbox-short.txt as the file to enter
fname = input("Enter file name: ")

fh = open(fname)
count = 0
hour = dict()

for line in fh:
    a = line.split()
    if len(a) > 2 and a[0] == "From":
        b = a[5].split(":")
        hour[b[0]] = hour.get(b[0], 0)+ 1


#print(hour)
tups = hour.items()

tups = sorted(tups)

for (key,val) in tups:
    print(key,val)


