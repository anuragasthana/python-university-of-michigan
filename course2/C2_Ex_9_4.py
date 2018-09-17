#Use mbox-short.txt as the file to enter
fname = input("Enter file name: ")

fh = open(fname)
count = 0
emails = dict()

for line in fh:
    l = line.split()
    if len(l) > 2:
        if l[0] == "From":
            emails[l[1]] = emails.get(l[1], 0) +1



largest = None
key = None

for i in emails:
    if largest is None or emails[i] > largest:
        largest = emails[i]
        key = i

print(key,largest)