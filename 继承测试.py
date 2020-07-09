

class A(object):

    def __init__(self,name):
        self.name = name
        print('执行A_init',self.name)


    def funA(self):
        print('执行funA')


class B(A):

    def __init__(self,name):

        # super(B, self).__init__()
        super().__init__(name)
        print('执行B_init')

    def funB(self):
        print('执行funB')
        self.funA()

b = B('xm')
b.funB()