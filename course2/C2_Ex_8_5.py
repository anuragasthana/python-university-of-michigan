#Use mbox-short.txt as the file to enter
fname = input("Enter file name: ")

fh = open(fname)
count = 0


for line in fh:
    l = line.split()

    if len(l) > 2:
        if l[0] == "From":
            count = count +1
            print(l[1])


print("There were", count, "lines in the file with From as the first word")