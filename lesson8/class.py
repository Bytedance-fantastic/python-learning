# encoding=utf8
#lesson8，对象，信息和信息处理的封装

class Numbers():
    # 初始化，python自动执行，初始化类的信息
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b
    # 私有方法，_开头
    def _minus(self, a, b):
        return a - b
    # 私有方法，只有内部才能使用
    def get_private_operator(self, a, b):
        return self._minus(a, b)

    def get_name(self):
        return self.name

if __name__ == '__main__':
    obj = Numbers("class_test")
    print(obj.add(1, 2))
    print(obj.div(6, 3))
    print(obj.get_name())
    print(obj.get_private_operator(2, 3))
