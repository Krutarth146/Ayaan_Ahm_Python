print("""
    Hi I am Ayaan.
    Royal 
    Techno
""")

print("Dhiraj",end=' ')
print("Sir")  # Dhiraj Sir


# Python is Dyanamic  (Run time), Interpreted (Line by Line)

kru_sir = 10
_1 = 20
ayaan  = 30

print(kru_sir, _1, ayaan,sep='___')  # 10___20___30

name = "Ayaan"
rupees = 800

print(name,"has",rupees,"Rs. only.")  # Ayaan has 800 Rs. only.
print(f"{name} has {rupees} Rs. only.")  # fstring (Adv. formatted String)
# Ayaan has 800 Rs. only.


str1 = "A"
print(type(str1))  # <class 'str'>

print("{} has {} Rupees only.".format("Ayaan", 900))   # Ayaan has 900 Rupees only.
print("{1} has {0} Rupees only.".format("Ayaan", 900))   # 900 has Ayaan Rupees only.
print("{name} has {rupees} Rupees only.".format(name= "Ayaan", rupees= 900))   # Ayaan has 900 Rupees only.

'''
sdvsdv
sd
vs
dv
sd
vs
'''

# x = 900
# y = input()

# print(x+ord(y))

# Typecasting  ---> 1. IMplicit T.C   2. Explicit T.C

x = 90   # Int
y = True   # bool
print(x+y)  # 91  # Implicit T.C

n = 23      # int
y = 21+9j   # Complex   # 21 is Real Part, 9j is Imah=ginary Part

# int, float, string, bool, complex, nonetype, list, tuple, set, dict

print(n+y)  # (44+9j)  Implicit


x = 21
y = '34'
print(x+int(y))  # 55    # Explicit T.C

k = 78
f = 67.89

print(k+f)  # 145.89


j = '45.89'
print(int(float(j)))  # 45

print(round(45.89)) # 46
print(round(45.89,2)) # 45.89
print(round(45.89,1)) # 45.9
print(round(45.89,0)) # 46.0
print(round(45.89,-1)) # 50.0
print(round(43.89,-1)) # 40.0
print(round(66.90,-2)) # 100.0
print(round(66.90,-3)) # 0.0



import math

print(math.floor(90.999))  # 90
print(math.ceil(90.001))  # 91
print(math.ceil(90.000))  # 90

import random


print(random.randint(1,6))

# Prime Number

# 3 ---> 1,3
# 23 ---> 1,23
# 29 ---> 1,29
# 24 ---> 1,2,3,4,6,8,12,24
# 42 ---> 1,2,3,6,7,14,21,42

num = 24
counter = 0

ayaan = 1
while ayaan <= num:
    if num % ayaan == 0:   # 24 % 3 == 0
        print(ayaan,end=' ')  # 1 2 3 ....
        counter+=1  # counter = counter + 1
    ayaan+=1

print("\nCounter = %d" %counter)

if counter == 2:
    print("Prime Number")