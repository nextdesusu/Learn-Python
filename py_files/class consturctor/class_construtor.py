import types

class SpecialClass(object):
    @classmethod
    def removeVariable(cls, name):
        return delattr(cls, name)

    @classmethod
    def addMethod(cls, func):
        return setattr(cls, func.__name__, types.MethodType(func, cls))

def hello(self, n):
    print(n)

instance = SpecialClass()
SpecialClass.addMethod(hello)
SpecialClass.hello("LEL")
