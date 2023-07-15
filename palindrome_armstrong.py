# 153 ----> 3*3*3 + 5*5*5 + 1*1*1
# 8208 ----> 8*8*8*8 + 0 + 2*2*2*2 + 8*8*8*8


# + - * / // % **

# print(25 / 2)  # 12.5
# print(25 // 2)  # 12
# print(25 % 2)  # 1
# print(-25 // 4)  # -7
# print(-25 ** 2)  # -625

# Armstrong

num = 8208
sum,counter = 0,0

xerox = num  # xerox = 153
safe = num  # xerox = 153

while safe != 0:
    safe = safe // 10
    counter += 1


while num > 0:  #  0 > 0  # False
    rem = num % 10   # 1
    # sum  = sum + rem ** len(str(xerox))   # sum = 27 + 125 + 1 = 153
    i = 1
    mul = 1
    while i <= counter:
        mul = mul * rem   # 3 * 3
        i+=1
    sum  = sum + mul   # sum = 27 + 125 + 1 = 153
    num = num // 10   # 0

print("sum = ",sum)  # 153
print("num = ",num)  # 0

if sum == xerox:  # 153 == 0
    print("Armstrong")