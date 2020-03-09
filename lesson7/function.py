# encoding=utf8
#lesson7，信息处理过程的封装


# a/b这个信息过程的封装
def div(a, b):
    c = a / b
    return c


# a+b这个信息处理过程的封装
def add(a, b):
    c = a + b
    return c

if __name__ == '__main__':
    # 调用add方法，返回1和2相加的结果
    a = add(1, 2)
    # 调用div方法，返回2除以3的结果
    b = div(2, 3)
    # 调用系统api，打印出结果
    print(a)
    print(b)