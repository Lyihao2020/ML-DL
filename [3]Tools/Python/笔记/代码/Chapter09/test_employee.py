# 测试雇员案例

import unittest
from employee import Employee

class TestEmployeeCase(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建了一个人Employee测试对象"""
        self.my_employee = Employee('Max', 'Steven', 50000)
        self.salary = 50000

    def test_give_default_raise(self):
        """测试默认年薪增量函数"""
        self.my_employee.give_raise()
        self.salary += 5000

        self.assertEquals(self.salary, self.my_employee.salary)

    def test_give_custom_raise(self):
        """测试指定年薪增量函数"""
        self.my_employee.give_raise(7500)
        self.salary += 7500

        self.assertEquals(self.salary, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()

