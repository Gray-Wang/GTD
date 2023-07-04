import unittest

"""
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。

Python 数据类型转换可以分为两种：

隐式类型转换 - 自动完成
显式类型转换 - 需要使用类型函数来转换
"""


class Demo3DataTypeConversion(unittest.TestCase):
    """
    隐式类型转换
    在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
    以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。
    """
    def test_implicit_type_conversion(self):
        num_int = 123
        num_flo = 1.23

        num_new = num_int + num_flo

        print("datatype of num_int:", type(num_int))
        print("datatype of num_flo:", type(num_flo))

        print("Value of num_new:", num_new)
        print("datatype of num_new:", type(num_new))
