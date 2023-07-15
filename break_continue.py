k=1

while k<=10:
    print(k,end=' ')  # 1 2 3 4 5
    if k == 5:
        break
    k+=1

print()

k = 10
while k<=15:
    if k == 13:
        k+=1
        continue
    print(k,end=' ')  # 10 11 12
    k+=1

print()


h = 25
while h <= 30:
    k = 25
    while k<=30:
        if h == k:
            break
        print(k,end=' ')
        k+=1
    print(h,end=' ')
    h+=1

# 25 25 26 25 26 27 25 26 27 28 25 26 27 28 29 25 26 27 28 29 30


print()
h = 25
while h <= 30:
    k = 25
    while k<=30:
        if h == k:
            k+=1
            continue
        print(k,end=' ')
        k+=1
    print(h,end=' ')
    h+=1

# 26 27 28 29 30 25 25 27 28 29 30 26 25 26 28 29 30 27 25 26 27 29 30 28 25 26 27 28 30 29 25 26 27 28 29 30 
print()
m = 1
while m <= 5:
    s = 1
    while s<4:
        if m <= s:
            s+=1
            continue
        print(s,end=' ')
        s+=1
    print(m,end=' ')
    m += 1 
# 1 1 2 1 2 3 1 2 3 4 1 2 3 5



