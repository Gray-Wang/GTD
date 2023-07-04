import unittest


class Demo4CodeComments(unittest.TestCase):
    """
    在 Python3 中，注释不会影响程序的执行，但是会使代码更易于阅读和理解。
    Python 中的注释有单行注释和多行注释。
    注意：多行注释可以嵌套使用，但是单行注释不能嵌套使用。
    """

    def test_one_line_comment(self):
        # 这是一个注释
        print("这个是单行注释")

    def test_two_line_comment(self):
        '''
        这是多行注释，用三个单引号
        这是多行注释，用三个单引号
        这是多行注释，用三个单引号
        '''

        """
        这是多行注释，用三个双引号
        这是多行注释，用三个双引号 
        这是多行注释，用三个双引号
        """
        print("这个是多行注释")
