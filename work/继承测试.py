


#父类

class testA(object):


    def __init__(self,a,b):
        self.a = 10
        self.b = 20
        print('testA_init')

    def funA(self):
        return ('funA')

class testB(testA):

    def __init__(self):
        # super.__init__()
        # self.a = 100
        # self.c = 300
        # super.__init__(a,b)
        print('testB_init')

    def funB(self):
        return ('funB')

# b1 = testB(1,2)
# print(b1.a)
# print(b1.b)
# print(b1.funB())
# print(b1.funA())

b2 = testB()