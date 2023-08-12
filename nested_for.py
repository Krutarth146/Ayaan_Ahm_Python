# # for i in range(5):
# #     print(i)

# for j in range(4):      # (0 to 3)  j = 0
#     for k in range(4):  # (0 to 3)  k = 0
#         if j == k:      # 
#             break
#         print(k,end=' ')   # 
#     print(j,end=' ')   # 

# # 0 0 1 0 1 2 0 1 2 3

for j in range(4):      # (0 to 3)  j = 1
    for k in range(4):  # (0 to 3)  k = 3
        if j == k:      # 1 == 3
            continue
        print(k,end=' ')   # 1 2 3 0 2 3
    print(j,end=' ')   # 0

# 


for j in range(4):      # (0 to 3)  j = 1
    for k in range(4):  # (0 to 3)  k = 3
        if j % k == 0:      
            continue
        print(k,end=' ')  
    print(j,end=' ') 

# 