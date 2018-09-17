import re
fname = input("Enter file name: ")
fh = open(fname)

all = ""

for line in fh:
    all = all + line

nums = re.findall('[0-9]+',all)

x = 0
for num in nums:
    x = x + int(num)

print(x)
