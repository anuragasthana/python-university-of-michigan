# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find("0")
        num = line[pos:]
        num = num.strip()
        fnum = float(num)
        total = total + fnum
        count = count + 1


average = total / count
print("Average spam confidence:", average)
