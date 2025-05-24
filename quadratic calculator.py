import math

#user input for values of equation
a = (input("a= "))
b = (input("b= "))
c = (input("c= "))

#value validity check
a_check = bool(a)
b_check = bool(b)
c_check = bool(c)

if not a_check:
    print("enter a value for 'a'")
if not b_check:
    print("enter a value for 'b'")
if not c_check:
    print("enter a value for 'c'")

#output
if a_check and b_check and c_check:
    a = int(a)
    b = int(b)
    c = int(c)
    x1 = (-b + math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    if x1 == x2:
        print(f"only one solution: {round(x1,3)}")
    else:
        print(round(x1,3))
        print(round(x2,3))
