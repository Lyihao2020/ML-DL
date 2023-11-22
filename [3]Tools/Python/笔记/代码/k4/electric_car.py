# 继承
from car import Car

# 使用代码模拟实物时，给类添加的细节越多越好：属性和方法清单以及文件都将越来越长
# 可能将类的一部分作为一个独立的类提取出来进行协作
class Battery():
    """一次模拟电动汽车电频的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电频的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电频容量的消息"""
        print(f'This car has a {str(self.battery_size)}-kWh battery.')

    def get_range(self):
        """打印一条信息，指出电频的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = ('This car can go approximately ' + str(range) +
                   ' miles on a full charge.')
        print(message)

    def update_battery(self):
        """检查电池的容量"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        self.gas_tank = None  # 在子类中定义一个与父类同名的属性，覆盖掉父类的属性

    def fill_gas_tank(self):
        """
        重写父类的方法：对于父类的方法，只要他不符合子类模拟的实物的行为，都可对其进行重写
        电动汽车没有油箱
        """
        print('This car doesn\'t need a gas tank!')

my_tesla = ElectricCar('tesla', 'model y', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()