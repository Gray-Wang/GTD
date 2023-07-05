import math
import random
import unittest

"""
Python3 数字(Number)
Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
"""


class Demo6NumberInfo(unittest.TestCase):
    """
    以下实例在变量赋值时 Number 对象将被创建：
    """

    def test_number(self):
        var1 = 1
        var2 = 10
        # 您也可以使用del语句删除一些数字对象的引用。
        # del var1[,var2[,var3[....,varN]]]
        del var1, var2

    """
    Python 支持三种不同的数值类型：

    整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
    
    浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    
    复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
    
    我们可以使用十六进制和八进制来代表整数：
    """

    def test_hexadecimal(self):
        number = 0xA0F  # 十六进制
        print(f"十六进制 number ： {number}")
        number = 0o37  # 八进制
        print(f"八进制 number ： {number}")

    """
    Python 数字类型转换
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    
    int(x) 将x转换为一个整数。
    
    float(x) 将x转换到一个浮点数。
    
    complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
    
    complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
    """

    def test_numeric_type_conversion(self):
        a = 1.0
        b = int(a)
        print(f"b 的类型为：{type(b)}")

    """
    Python 数字运算
    Python 解释器可以作为一个简单的计算器，您可以在解释器里输入一个表达式，它将输出表达式的值。
    
    表达式的语法很直白： +, -, * 和 /, 和其它语言（如Pascal或C）里一样。例如：
    """

    def test_number_crunching(self):
        print(f"2 + 2 = {2 + 2}")
        print(f"50 - 5*6 = {50 - 5 * 6}")
        print(f"(50 - 5*6) / 4 = {(50 - 5 * 6) / 4}")
        print(f" 8 / 5 = {8 / 5}")  # 总是返回一个浮点数
        # 注意：在不同的机器上浮点运算的结果可能会不一样。
        #
        # 在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
        n = 17 / 3  # 整数除法返回浮点型
        print(f"整数除法返回浮点型:{n}")
        m = 17 // 3  # 整数除法返回向下取整后的结果
        print(f"整数除法返回向下取整后的结果:{m}")
        x = 17 % 3  # ％操作符返回除法的余数
        print(f"％操作符返回除法的余数:{x}")
        y = 5 * 3 + 2
        print(y)
        # 注意：// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
        print(f"7 // 2 = {7 // 2}")
        print(f"7.0//2 = {7.0 // 2}")
        print(f"7//2.0 = {7 // 2.0}")
        # Python 可以使用 ** 操作来进行幂运算：
        print(f"5 的平方={5 ** 2}")
        print(f"2的7次方={2 ** 7}")
        # 变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：
        # >>> n   # 尝试访问一个未定义的变量
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # NameError: name 'n' is not defined
        # 不同类型的数混合运算时会将整数转换为浮点数：
        print(f"3 * 3.75 / 1.5 = {3 * 3.75 / 1.5}")
        print(f"7.0 / 2 = {7.0 / 2}")

    """
    数学函数
    """

    def test_math_func(self):
        print(f"-10的绝对值是：{abs(-10)}")
        print(f"4.1向上取整是：{math.ceil(4.1)}")
        print(f"e的1次幂是：{math.exp(1)}")
        print(f"-10的绝对值(浮点数形式)是：{math.fabs(-10)}")
        print(f"10.9向下取整是：{math.floor(10.9)}")
        print(f"求对数 10的多少次幂等于100？ {math.log(100, 10)}")
        print(f"返回以10为基数的x的对数 {math.log10(100)}")
        print(f"参数的最大值，参数可以为序列。{max(1, 2, 3, 4, 6)}")
        print(f"参数的最小值，参数可以为序列。{min(1, 2, 3, 4, 6)}")
        print(f"返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 {math.modf(10.89)}")
        print(f"5的5次幂是{5 ** 5}")
        print(
            f"返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。 {round(70.23456)}")
        print(f"2的平方根是{math.sqrt(4)}")

    """
    随机数函数
    随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
    
    Python包含以下常用随机数函数：
    """

    def test_random_func(self):
        n = random.choice(range(10))  # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
        print(n)
        # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
        print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
        # 第一个随机数
        print("random() : ", random.random())
        # 第二个随机数
        print("random() : ", random.random())
        random.seed()
        print("使用默认种子生成随机数：", random.random())
        print("使用默认种子生成随机数：", random.random())
        list = [20, 16, 10, 5];
        random.shuffle(list)
        print("随机排序列表 : ", list)
        print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
        print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))

    """
    三角函数
    """

    def test_trigonometric_func(self):
        print("acos(0.64) : ", math.acos(0.64))  # 返回0.64的反余弦弧度值。
        print("asin(0.64) : ", math.asin(0.64))  # 反正弦弧度值。
        print("atan(0.64) : ", math.atan(0.64))  # 反正切弧度值
        print("atan2(-0.50,-0.50) : ", math.atan2(-0.50, -0.50))  # 返回给定的 X 及 Y 坐标值的反正切值。
        print("cos(3) : ", math.cos(3))  # 返回x的弧度的余弦值。
        print("hypot(3, 2) : ", math.hypot(3, 2))  # 返回欧几里德范数 sqrt(x*x + y*y)。
        print("sin(3) : ", math.sin(3))  # 返回的x弧度的正弦值。
        print("(tan(3) : ", math.tan(3))  # 返回x弧度的正切值。
        print("degrees(3) : ", math.degrees(3))  # 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
        print("radians(90) : ", math.radians(90))  # 将角度转换为弧度 1 弧度等于大概 57.3°
