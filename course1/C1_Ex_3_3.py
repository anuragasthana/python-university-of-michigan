score = input("Enter Score: ")
try:
    sc = float(score)
except:
    print("No number has been printed")
    quit()
if sc < 0.0:
    print("Number is out of range")
    quit()
elif sc > 1.1:
    print("Number is out of range")
    quit()
elif sc >= 0.9 :
    print("A")
elif sc >= 0.8 :
    print("B")
elif sc >= 0.7 :
    print("C")
elif sc >= 0.6 :
    print("D")
elif sc < 0.6 :
    print("F")
