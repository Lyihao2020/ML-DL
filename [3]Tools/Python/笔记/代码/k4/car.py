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
