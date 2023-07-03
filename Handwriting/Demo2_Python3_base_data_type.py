import unittest


"""
标准数据类型
Python3 中常见的数据类型有：

Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。
"""

class Study_2(unittest.TestCase):
    """
    Python3 基本数据类型
    Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
    等号（=）用来给变量赋值。
    等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
    """
    def test_base_data_type(self):
        counter = 100  # 整型变量
        miles = 1000.0  # 浮点型变量
        name = "runoob"  # 字符串
        print(counter)
        print(miles)
        print(name)

        '''
        多个变量赋值
        Python允许你同时为多个变量赋值。例如：
        '''
        a = b = c = 1

        '''
        以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
        您也可以为多个对象指定多个变量。例如：
        '''
        a, b, c = 1, 2, "runoob"

        '''
        以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
        '''

    """
    Number（数字）
    Python3 支持 int、float、bool、complex（复数）。
    在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    像大多数语言一样，数值类型的赋值和计算都是很直观的。
    内置的 type() 函数可以用来查询变量所指的对象类型。
    """
    def test_Number_2(self):
        a, b, c, d = 20, 5.5, True, 4 + 3j
        print(type(a), type(b), type(c), type(d))

        # 此外还可以用 isinstance 来判断：
        f = 111
        print(f"变量f是int类型 ？  答： {isinstance(f, int)}")
        '''
        isinstance 和 type 的区别在于：
        type()不会认为子类是一种父类类型。
        isinstance()会认为子类是一种父类类型。
        '''
        print(type(c) == int)
        print(isinstance(c, int))
        '''
        注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
        '''
        print(issubclass(bool, int))

        print(True + 1)
        print(False + 1)
        print(1 is True)
        print(0 is False)

    '''
    当你指定一个值时，Number 对象就会被创建：
    您也可以使用del语句删除一些对象引用。
    del语句的语法是：
    '''
    def test_del_1(self):
        var1 = 1
        var2 = 10
        del var1, var2
