num = 24

op = 2

while op<num:   # 2 to 23
    if 24 % op == 0:   # 24 % 2 == 0
        break
    op+=1  # op = op + 1

if num == op:   # 24 == 2
    print("Prime")

# ------------------------

num = 7321  # -----> 1237

while num > 0:
    rem = num % 10    # rem = 7
    print(rem,end='')  # 1237
    num = num // 10  # num = 0

print()

# Sum of Digits
num = 972432
sum = 0

while num > 0:
    rem = num % 10    # rem = 7
    if rem % 2 == 1:
        sum = sum + rem   # sum = 19
    num = num // 10  # num = 0

print(sum)


# Sum of Digits
num = 999999
counter = 0

while num > 0:
    num = num // 10  # num = 0
    counter += 1
print(counter)  # 6




# Sum of Digits
num = 151
sum = 0

while num > 0:
    rem = num % 10    # rem = 9
    sum = sum + rem    # sum = 151
    num = num // 10  # num = 0

print(sum)