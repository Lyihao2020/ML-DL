# 使用类和实例

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 类中的每个属性都必须有初始值，哪怕为0或者空字符串
        self.gas_tank = 100

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """更新里程表读数"""
        if mileage >= self.odometer_reading:
            print(f'Updating mileage from {self.odometer_reading} to {mileage}.')
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            print(f'Odometers have increased {miles} miles.')
            self.odometer_reading += miles
        else:
            print('You can\'t roll back an odometer!')

    def fill_gas_tank(self):
        """填满汽车的油箱"""
        if self.gas_tank < 100:
            self.gas_tank = 100
        print('This car\'s gas tank is full.')

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

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    """
    但如果一个方法或者属性是任何汽车都有的，而不是电动汽车特有的
    就应该将其加入Car类而不是子类中
    """
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_new_car.update_odometer(100)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(5)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(-2)
    my_new_car.read_odometer()
    my_new_car.gas_tank = 70
    print(my_new_car.gas_tank)
    my_new_car.fill_gas_tank()
    print(my_new_car.gas_tank)
