'''
100以内的质数

1-什么质数-只能被1和他本身整除的数

2-让这个数从1开始整除，一直整除到他本身，期间如果发现有被其他数整除，则说明不是质数

3-将其变成循环，判断100以内的每一个数


'''


arr = list(range(1,101))
new_arr = []

for j in arr:
    if j == 1:
        continue
    else:
        for i in range(2,j):
            if j % i == 0:
                # print('不是质数')
                break
        else:
            new_arr.append(j)


print('质数列表：',new_arr)