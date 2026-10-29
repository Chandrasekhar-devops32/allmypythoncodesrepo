m = int(input("marks in maths:"))
s = int(input("marks in science:"))
e = int(input("marks in english:"))
t = m+s+e
ave = t/3
print(f"total marks is : {t}")
print(f" average marks is :{ave}")
if ave >86 :
    print("grade : A")
else:
    print("grade :B")
    