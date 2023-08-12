# for(i=0;i<10;i++)
# {
#     printf("%d",i);
# }

for ayaan in range(10):   # 0 1 2 3 4 5 6 7 8 9
    print(ayaan,end=' ')   # start = 0, end = 10(n-1) = 9

print()

for j in range(2,9):
    print(j,end=' ')  # 2 3 4 5 6 7 8 
print()

for j in range(9,2):
    print(j,end=' ')  # blank

print()

for k in range(4,14,1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # 4 5 6 7 8 9 10 11 12 13
print()

for k in range(4,14,2):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # 4 6 8 10 12

print()

for k in range(4,14,-1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # blank

print()

for k in range(-3,4,1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # -3 -2 -1 0 1 2 3

print()

for k in range(-9,-2,1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # -9 -8 -7 -6 -5 -4 -3
print()

for k in range(5,1,-2):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # 5 3
print()

for k in range(-2,2,3):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # -2 1
print()

for k in range(3,-3,-3):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # 3,0
print()

for k in range(-3,4,-1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # blank
print()

for k in range(-2,-5,-1):  # (start, End(n-1), step(n-1))
    print(k,end=' ')  # -2 -3 -4

# --------------------------------------------------
# choice = 10

# match choice:

#     case 10: print("1")

#     case '20.90': print("20.90")

#     case 'x': print("Invalid Choice")



# int a[5]

print(ord('D'))   # 68
print(ord('z'))   # 122
print(chr(121))   # y

list1 = [20,90.89,'str1',[(10,20,30), [10,20]], {10,20,30,10}, {'Name' : "Ayaan", 'school' : 'Shanti'}]


print(list1)   # [20, 90.89, 'str1', [(10, 20, 30), [10, 20]], {10, 20, 30}, {'Name': 'Ayaan', 'school': 'Shanti'}]


for ayaan in list1:
    print(ayaan)

# for h in range(6):
for h in range(len(list1)):
    print(list1[h])


l3 = [10,90,78.453, 32, 45, 12]

