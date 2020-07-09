'''
4.士兵开枪
需求：
1）.士兵的名字叫瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是枪的扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

解析:

类：
    士兵 soldier

属性：
    名字 name（瑞恩）

方法：
    开火 fire
    实现：调用枪这个类的发射子弹的方法
#---------------------------------
类：
    枪

属性：
    名字 name AK47
    子弹 bullet 0
方法：
    发射
        子弹减少-1
    装填
        子弹增多+10
'''


#     类：
#     士兵
#     soldier
class Soldier(object):
    #
    # 属性：
        # 名字
        # name（瑞恩）
    def __init__(self,name):
        self.name = name

    # 方法：
    # 开火    item = g
    # fire
    def fire(self,item):
        # 实现：调用枪这个类的发射子弹的方法
        print('扣动{}扳机，发射子弹'.format(item.name))
        item.shot()
        print('开火后，子弹还剩{}颗'.format(item.bullet))

    def __str__(self):
        return "士兵的名字{}".format(self.name)

# 类：
#     枪 gun
class Gun(object):
    #
    # 属性：
    #     名字 name AK47
    #     子弹 bullet 0
    def __init__(self,name):
        self.name = name
        self.bullet = 0

    # 方法：
    #     发射
    #         子弹减少-1
    def shot(self):
        if self.bullet > 0:
            print('发射子弹，子弹减少一颗')
            self.bullet -= 1
        else:
            print('没子弹了')
    #     装填
    #         子弹增多+10
    def load(self):
        print('装填子弹，一次10发')
        self.bullet += 10



    def __str__(self):
        return "{}枪现在有{}发子弹".format(self.name,self.bullet)


if __name__ == '__main__':
    '''
    1）.士兵的名字叫瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是枪的扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
    '''
    #实例化
    g = Gun('AK47')
    # g.shot()
    g.load()
    # g.shot()
    print(g)
    #
    s = Soldier('瑞恩')
    s.fire(g)
    # print(s)
