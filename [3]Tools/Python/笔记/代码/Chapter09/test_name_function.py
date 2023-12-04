"""
Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实两数的某个方面设有问题;
测试用例是一组单元测试，这些单元测试一起核实两数在各种情形下的行为都符合要求。
良好的测试用例考虑到了函数可能收到的各种输人，包含针对所有这些情形的测试。
全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的两数使用方式。
对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项日被广泛使用时再考虑全覆盖。
可通过的测试：创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对两数的单元调试就很简单了。
要为两数编写测试用例，可先导人模块unittest以及要测试的两数，再创建一个继承unittest.TestCase的类，并编写一系列方法对两数行为的不同方面进行测试。
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self): # 再运行test_name_function.py后，所有test_打头的方法都将自动运行
        """能正确处理一些常见姓名"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')   # 断言方法来核实得到的结果是否与期望的结果相一致

    def test_first_last_middle_name(self):
        """能正确处理一些带有中间名的常见姓名"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEquals(formatted_name, 'Wolfgang Amadeus Mozart')   # 断言方法来核实得到的结果是否与期望的结果相一致

if __name__ == '__main__':
    unittest.main()
