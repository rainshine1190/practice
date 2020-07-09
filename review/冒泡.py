
#while循环实现冒泡排序

# a = [1,3,4,5,0,2,6]
# n = 0
# while n<len(a):
#     m = 1
#     while m<len(a)-n:
#         if a[m] < a[m-1]:
#             temp = a[m]
#             a[m] = a[m-1]
#             a[m-1] = temp
#
#         m += 1
#     n += 1
# print(a)


#for循环实现冒泡

a = [1,3,4,5,0,2,6]

for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j] < a[j-1]:
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp

print(a)