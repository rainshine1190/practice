#快速排序

#设定一个中间值作为基准m，设定一个low坐标，一个high坐标
# 然后用数组中的所有元素与改值比较，大的放到right，high-1，小的放到left，low+1
#直到low比high大


a = [8,1,7,2,6,3,5,2,1,0]


def paixu(a):
    print(len(a))
    if len(a)>=2:
        mid = a[len(a)//2]
    else:
        return a
    print('mid',mid)

    low = 0
    high = len(a)-1
    n = 0
    right = []
    left = []

    while low <= high:
        if a[n] >= a[mid]:
            right.append(a[n])
            high -= 1
        else:
            left.append(a[n])
            low += 1
        n += 1
    arr = paixu(left)+list(a[mid])+paixu(right)

    return arr

print(paixu(a))