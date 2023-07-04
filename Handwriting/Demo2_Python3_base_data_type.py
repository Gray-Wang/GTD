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
        # print(1 is True)
        # print(0 is False)

    '''
    当你指定一个值时，Number 对象就会被创建：
    您也可以使用del语句删除一些对象引用。
    del语句的语法是：
    '''

    def test_del_1(self):
        var1 = 1
        var2 = 10
        del var1, var2

    """
    数值运算
    """

    def test_numerical_operations(self):
        print(f"5 + 4 = {5 + 4} # 加法")
        print(f"4.3 - 2 = {4.3 - 2} # 减法")
        print(f"3 * 7 = {3 * 7} # 乘法")
        print(f"2 / 4 = {2 / 4}  # 除法，得到一个浮点数")
        print(f"2 // 4 = {2 // 4} # 除法，得到一个整数")
        print(f"17 % 3 = {17 % 3} # 取余")
        print(f"2 ** 5 = {2 ** 5} # 乘方")

    """
    字符串操作
    """

    def test_String_1(self):
        str = 'Runoob'

        print(str)  # 输出字符串
        print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
        print(str[0])  # 输出字符串第一个字符
        print(str[2:5])  # 输出从第三个开始到第五个的字符
        print(str[2:])  # 输出从第三个开始的后的所有字符
        print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
        print(str + "TEST")  # 连接字符串

        print("Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：")
        print('Ru\noob')
        print(r'Ru\noob')
        '''
        另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 \'''...\''' 跨越多行。
        注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
        '''
        word = 'Python'
        print(word[0], word[5])
        print(word[-1], word[-6])
        '''
        与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。
        注意：
            1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
            2、字符串可以用+运算符连接在一起，用*运算符重复。
            3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
            4、Python中的字符串不能改变。
        '''

    """
    bool（布尔类型）
        布尔类型即 True 或 False。
        
        在 Python 中，True 和 False 都是关键字，表示布尔值。
        
        布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。
        
        布尔类型特点：
        
        布尔类型只有两个值：True 和 False。
        
        布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。
        
        布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。
        
        布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。
    """

    def test_bool(self):
        a = True
        b = False

        # 比较运算符
        print(2 < 3)  # True
        print(2 == 3)  # False

        # 逻辑运算符
        print(a and b)  # False
        print(a or b)  # True
        print(not a)  # False

        # 类型转换
        print(int(a))  # 1
        print(float(b))  # 0.0
        print(str(a))  # "True"
        '''
        注意: 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
        '''

    """
    List（列表）
        List（列表） 是 Python 中使用最频繁的数据类型。
        
        列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
        
        列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
        
        和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
        
        列表截取的语法格式如下：
        
        变量[头下标:尾下标]
        索引值以 0 为开始值，-1 为从末尾的开始位置。
    """

    def test_List(self):
        # 加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：
        list = ['abcd', 786, 2.23, 'runoob', 70.2]
        tinylist = [123, 'runoob']

        print(list)  # 输出完整列表
        print(list[0])  # 输出列表第一个元素
        print(list[1:3])  # 从第二个开始输出到第三个元素
        print(list[2:])  # 输出从第三个元素开始的所有元素
        print(tinylist * 2)  # 输出两次列表
        print(list + tinylist)  # 连接列表
        # 与Python字符串不一样的是，列表中的元素是可以改变的：
        a = [1, 2, 3, 4, 5, 6]
        a[0] = 9
        a[2:5] = [13, 14, 15]
        print(a)
        a[2:5] = []  # 将对应的元素值设置为 []
        print(a)
        '''
        List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。
        注意：
        1、List写在方括号之间，元素用逗号隔开。
        2、和字符串一样，list可以被索引和切片。
        3、List可以使用+操作符进行拼接。
        4、List中的元素是可以改变的。
        Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
        '''

    """
    如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
    """

    def test_reverseWords(self):
        input = "I love you"
        # 通过空格将字符串分隔符，把各个单词分隔为列表
        inputWords = input.split(" ")

        # 翻转字符串
        # 假设列表 list = [1,2,3,4],
        # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
        # inputWords[-1::-1] 有三个参数
        # 第一个参数 -1 表示最后一个元素
        # 第二个参数为空，表示移动到列表末尾
        # 第三个参数为步长，-1 表示逆向
        inputWords = inputWords[-1::-1]

        # 重新组合字符串
        output = ' '.join(inputWords)
        print(output)

    """
    Tuple（元组）
        元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
        
        元组中的元素类型也可以不相同：
    """

    def test_Tuple(self):
        tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
        tinytuple = (123, 'runoob')

        print(tuple)  # 输出完整元组
        print(tuple[0])  # 输出元组的第一个元素
        print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
        print(tuple[2:])  # 输出从第三个元素开始的所有元素
        print(tinytuple * 2)  # 输出两次元组
        print(tuple + tinytuple)  # 连接元组

        # 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
        # 其实，可以把字符串看作一种特殊的元组。
        tup = (1, 2, 3, 4, 5, 6)
        print(tup[0])
        print(tup[1:5])
        # 修改元组元素的操作是非法的
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # TypeError: 'tuple' object does not support item assignment
        # tup[0] = 11

        '''
        虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
        构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
        '''
        tup1 = ()  # 空元组
        tup2 = (20,)  # 一个元素，需要在元素后添加逗号
        '''
        string、list 和 tuple 都属于 sequence（序列）。
        注意：
            1、与字符串一样，元组的元素不能修改。
            2、元组也可以被索引和切片，方法一样。
            3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
            4、元组也可以使用+操作符进行拼接。
        '''

    '''
    Set（集合）
        集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
        set是无序不重复元素的序列。
        基本功能是进行成员关系测试和删除重复元素。
        可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
        创建格式：
            parame = {value01,value02,...}
            或者
            set(value)
    '''

    def test_Set(self):
        # 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
        set_var = set()
        # 非空集合 可以使用大括号 { } 或者 set() 函数创建集合
        sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
        print(sites)  # 输出集合，重复的元素被自动去掉

        # 成员测试
        if 'Runoob' in sites:
            print('Runoob 在集合中')
        else:
            print('Runoob 不在集合中')

        # set可以进行集合运算
        a = set('abracadabra')
        b = set('alacazam')

        print(a)

        print(a - b)  # a 和 b 的差集

        print(a | b)  # a 和 b 的并集

        print(a & b)  # a 和 b 的交集

        print(a ^ b)  # a 和 b 中不同时存在的元素
        # set()参数可以是列表，元组，字典等
        person2 = set(("hello", "jerry", 133, 11, 133, "jerru"))
        print(person2)
        # set是无序不重复元素的序列。
        person3 = {"hello", "jerry", 133, 11, 133, "jerru"}
        print(person3)

    '''
    Dictionary（字典）
        字典（dictionary）是Python中另一个非常有用的内置数据类型。
        
        列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        
        字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
        
        键(key)必须使用不可变类型。
        
        在同一个字典中，键(key)必须是唯一的。
    '''

    def test_Dictionary(self):
        dict = {}
        dict['one'] = "1 - 菜鸟教程"
        dict[2] = "2 - 菜鸟工具"

        tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

        print(dict['one'])  # 输出键为 'one' 的值
        print(dict[2])  # 输出键为 2 的值
        print(tinydict)  # 输出完整的字典
        print(tinydict.keys())  # 输出所有键
        print(tinydict.values())  # 输出所有值

        # 构造函数 dict() 可以直接从键值对序列中构建字典如下：
        lst = [('Runoob', 1), ('Google', 2), ('Taobao', 3)]
        '''
        以下代码会报错，原因及解决方案如下：
        在上述代码中，`dict`是Python内置的字典类型，它是一个类对象。在第1行中我们创建了一个变量`dict`并将其赋值为空字典。但是，与此同时，
        Python解释器也将`dict`作为类对象来绑定。在第11行中，我们尝试使用`dict()`函数来创建一个新的字典对象，并将其赋值给`dic_var`。然而，
        由于上述我们已经将名称`dict`与一个字典对象绑定，所以在此处尝试调用`dict()`函数会导致`TypeError`异常。
        为了解决这个问题，你可以将变量`dict`重命名为其他名称，以避免与内置的`dict`函数产生冲突。例如，修改第1行的代码为`my_dict = {}`。
        '''
        dic_var = dict(lst)
        print(dic_var)
        # 也可以用推导式来创建字典
        dic_var2 = {x: x ** 2 for x in (2, 4, 6)}
        print(dic_var2)

    '''
    在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。
    与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
    bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
    '''

    def test_bytes(self):
        # 创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
        # 此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。
        # bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
        x = bytes("hello", encoding="utf-8")
        # 与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。同时，
        # 由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。例如：
        x = b"hello"
        y = x[1:3]  # 切片操作，得到 b"el"
        z = x + b"world"  # 拼接操作，得到 b"helloworld"
        # 需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。例如：
        x = b"hello"
        # ord() 函数用于获取指定字符的整数值
        if x[0] == ord("h"):
            print("The first element is 'h'")
