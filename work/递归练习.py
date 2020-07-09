"""
阶乘

1.5*4*3*2*1

n*n-1
直到1

"""

# 定义一个类(num是需要给出的参数)
# 一定要有临界值
# 要有递推的关系
def digui(num):

    # 打印num
    print('$'+str(num))

    # 如果num大于0
    if num > 0:
        # 调用自己每次减一
        digui(num - 1)
    # 否则
    else:
        # 打印*20次(用来分割线)
        print("*" * 20)

    # 打印num
    print('$'+str(num))

digui(3)
