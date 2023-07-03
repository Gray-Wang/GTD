import keyword
import unittest


class Study_1(unittest.TestCase):
    """
    保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
    """
    def test_show_keyword(self):
            print(keyword.kwlist)

    """
    Python中单行注释以 # 开头，实例如下：
    """
    def test_annotation(self):
        # 第一个注释
        print("Hello, Python!")  # 第二个注释
        # 第一个注释
        # 第二个注释

        '''
        第三注释
        第四注释
        '''

        """
        第五注释
        第六注释
        """
        print("Hello, Python!")

    """
    行与缩进
    python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
    
    缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
    """
    def test_line_and_indents(self):
        if True:
            print("True")
        else:
            print("False")
        return 0
        # 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
        # if True:
        #     print ("Answer")
        #     print ("True")
        # else:
        #     print ("Answer")
        # print ("False")    # 缩进不一致，会导致运行错误

    """
    多行语句   python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
    """
    def test_multiline_statement(self):
        total = "item_one" + \
                "item_two" + \
                "item_three"
        print(total)
        # 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
        total = ['item_one', 'item_two', 'item_three',
                 'item_four', 'item_five']
        print(total)

    """
    数字(Number)类型
    python中数字有四种类型：整数、布尔型、浮点数和复数。
        int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
        bool (布尔), 如 True。
        float (浮点数), 如 1.23、3E-2
        complex (复数), 如 1 + 2j、 1.1 + 2.2j
    """
    def test_number(self):
        int_var = 1
        print(f"int_var的数据类型是{type(int_var)}.")
        bool_var = True
        print(f"bool_var的数据类型是{type(bool_var)}.")
        float_var = 3E-2
        print(f"float_var的数据类型是{type(float_var)}.")
        complex_var = 1.1 + 2.2j
        print(f"complex_var的数据类型是{type(complex_var)}.")


    """
    字符串(String)
        Python 中单引号 ' 和双引号 " 使用完全相同。
        使用三引号(''' 或 \""")可以指定一个多行字符串。
        转义符 \。
        反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
        按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
        字符串可以用 + 运算符连接在一起，用 * 运算符重复。
        Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
        Python 中的字符串不能改变。
        Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
        字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
    """
    def test_string(self):
        word = '字符串'
        sentence = "这是一个句子。"
        paragraph = """这是一个段落，
        可以由多行组成"""
        print(paragraph)
        # 切片操作示例如下：
        str = '123456789'
        print(str)  # 输出字符串
        print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
        print(str[0])  # 输出字符串第一个字符
        print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
        print(str[2:])  # 输出从第三个开始后的所有字符
        print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
        print(str * 2)  # 输出字符串两次
        print(str + '你好')  # 连接字符串

        print('------------------------------')

        print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
        print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    """
    等待用户输入
    执行下面的程序在按回车键后就会等待用户输入：
    """
    def test_input(self):
        inp = input("\n\n按下 enter 键后退出。")
        print(f"inp = {inp}")
    """
    同一行显示多条语句
    Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
    """
    def test_same_line_multiple_statements(self):
        import sys;x = 'runoob';sys.stdout.write(x + '\n')

    """
    print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
    """
    def test_print(self):
        print("111", end=" ")
        print("1222")

    """
    import 与 from...import
    在 python 用 import 或者 from...import 来导入相应的模块。
    将整个模块(somemodule)导入，格式为： import somemodule
    从某个模块中导入某个函数,格式为： from somemodule import somefunction
    从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
    将某个模块中的全部函数导入，格式为： from somemodule import *
    """
    def test_import(self):
        from sys import argv, path  # 导入特定的成员
        print('================python from import===================================')
        print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

