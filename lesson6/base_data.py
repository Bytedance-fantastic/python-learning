# encoding=utf8
#lesson 1，基础类型

# 两种基础类型：
    # 数值：包括，整型（整数）和浮点型（小数）
    # 字符串

# 主函数，程序的入口
if __name__ == '__main__':
    # 整数
    a = 1
    # 小数
    b = 2.1
    # 字符串
    c = "hello world"
    # 变量可以相互赋值
    a = b

    # 打印内容
    print(a)
    print(b)
    print(c)

    print("*********分隔符1**********")
    # d是个变量，我们可以一直对他赋值，后面的值会覆盖签前面的值。
    # 数值计算，加减乘除
    d = a + b
    print(d)
    d = a - b
    print(d)
    d = a / b
    print(d)
    d = a * b
    print(d)

    print("*********分隔符2**********")

    # 字符串拼接
    d = c + " code world "
    print(d)
    d = "this is my first code " + ", hahah "
    print(d)

    # 字符串和数值拼接，整体为字符串
    d = "%s ,%s" % (c, a)
    print(d)
    d = "test for a number, %s " % (a)
    print(d)

    # 数值和字符串不能直接相加，不然会报错，取消注释运行一下
    # d = c + a
    # print(d)