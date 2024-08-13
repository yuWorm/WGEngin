from abc import ABCMeta


class TestMetaClass(ABCMeta):
    def __new__(cls, name, bases, attrs):
        print("调用了元类")
        print(name, bases, attrs)


class TestClass:
    test: int
    test2: int

    query = ["的"]

    def hhh(self):
        pass

    @classmethod
    def kkk(cls):
        pass

    @staticmethod
    def ssss():
        pass


a = TestClass()
print(a)
