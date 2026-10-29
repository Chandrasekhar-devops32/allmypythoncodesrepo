a = input()
x,y,z =  a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1>num2 :
    if num1>num3 :
        print(f"greatest is :{num1} ")
    else :
        print(f" greatest is :{num3} ")
elif num2>num1 :
    if num2>num3 :
        print(f"greatest is :{num2}")
    else :
        print(f"greatest is {num3}")
elif num3>num1 :
    if num3>num2:
        print(f"greatest is : {num3}")
    else :
        print(f"greatest is : {num2}")

