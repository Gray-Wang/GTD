import unittest
from faker import Faker
import pandas as pd
from prettytable import PrettyTable

faker = Faker(locale='zh_CN')


class testPyMethod(unittest.TestCase):

    """
        生成测试数据的excel，示例：
        +--------+-------------+--------------------+
        |  姓名  |    手机号   |       身份证       |
        +--------+-------------+--------------------+
        |  韩荣  | 15215683709 | 140902198201110097 |
        | 高秀梅 | 15380629326 | 532922198405220319 |
        +--------+-------------+--------------------+
        :param:  generateNum则为生成条数
    """

    def test_generate_excel(self):
        # 修改生成测试excel的行数
        generateNum = 5
        data = [[], [], []]
        for i in range(generateNum):
            data[0].append(faker.name())
            data[1].append(faker.phone_number())
            data[2].append(faker.ssn())

        dfData = {  # 用字典设置DataFrame所需数据
            '姓名': data[0],
            '手机号': data[1],
            '身份证号': data[2]
        }
        df = pd.DataFrame(dfData)  # 创建DataFrame
        df.to_excel('excelOutPutPath/text.xlsx', index=False)  # 存表，去除原始索引列（0,1,2...）

    """
    随机公司服务名
    """

    def test_generate_bs(self):
        table = PrettyTable(["随机公司服务名", "随机公司名（长）", "上级单位名", "地址"])
        for i in range(20):
            table.add_row([faker.bs(), faker.company(), faker.company(), faker.address()])
        print(table)

    """
    生成随机姓名手机号身份证号,示例如下：
    +--------+--------------------+-------------+
    |  姓名  |       身份证       |    手机号   |
    +--------+--------------------+-------------+
    |  马彬  | 150926197911141515 | 13054427222 |
    | 仲建军 | 532600195005051490 | 13190841218 |
    +--------+--------------------+-------------+
    """

    def test_generate_name_ssn_phone(self):
        table = PrettyTable(["姓名", "身份证", "手机号"])
        for i in range(2):
            table.add_row([faker.name(), faker.ssn(), faker.phone_number()])
        print(table)

    """
    随机生成段落
    """

    def test_generate_paragraph(self):
        print(faker.paragraph())


