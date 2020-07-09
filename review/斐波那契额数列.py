'''
需求：求xxx数列，1,1,2,3,5,8,13

分析：第三个数是前两个数之和（前两个数除外）

    a,b,c,d
    a = 1
    b = 1
    c = a+b  2

    a = b
    b = c
    d = a+b  3

             5


'''

a = b = 1
arr = []
n = int(input())
for i in range(n):
    arr.append(a)
    c = a + b
    a = b
    b = c

print(arr)