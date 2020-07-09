


# class A(object):
#
#     def funA(self):
#
#         print('funA')
#
#     def __funB(self):
#         print('funB')
#
# a = A().funA()
# b = A()
# b.__funB()


# import six
# #
# #
# # class SingletonType(type):
# #
# #     def __call__(cls, *args, **kwargs):
# #         if not hasattr(cls, "_instance"):
# #             cls.Instance = super(SingletonType, cls).__call__(*args, **kwargs)
# #
# #         return cls.Instance
# #
# #
# # @six.add_metaclass(SingletonType)
# # class IService:
# #

class Person(object):


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):

        if value < 0 or value > 100:
            raise ValueError

        self._score = value

p = Person()
p.score = 20
print(p.score)