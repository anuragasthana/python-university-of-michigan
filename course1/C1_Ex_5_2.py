largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        current = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = current
    elif current < smallest:
        smallest = current
    if largest is None:
        largest = current
    elif current > largest:
        largest = current

print("Maximum is", largest)
print("Minimum is", smallest)