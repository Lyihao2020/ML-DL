# 创建类
class Cat():
    def __init__(self, name):
        self.name = name

    def jump(self):
        print("{0} is jumping".format(self.name))

# 用类创建实例
my_cat = Cat("Loser")
your_cat = Cat("Lucky")

print(my_cat.name)
print(your_cat.name)

my_cat.jump()
your_cat.jump()

# 类的定义
# 要有实际意义
# 驼峰命名法：组成单词字母首字母大写
# class 类名:
# 类的属性
# def __init__(self, 要传递类的参数)   初始化类的属性
# 类的方法
"""类前空两行"""

class Car():
    """对类的简单介绍"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0    # 初始化汽车的里程数

    def get_main_information(self): # self不能省
        """获取汽车的主要信息"""
        print("brand: {0}, model: {1}, year: {2}".format(self.brand, self.model, self.year))

    def get_mileage(self):
        return "mileage: {}".format(self.mileage)

    # 禁止里程数为负
    def set_mileage(self, distance):
        if distance < 0:
            print("Wrong Input!")
        else:
            self.mileage = distance

    def increment_mileage(self, distance):
        """总里程数累加"""
        if distance > 0:
            self.mileage += distance
        else:
            print("Wrong Input!")

"""类后空两行"""

# 新的电动汽车的类
class ElectricCar(Car):
    """模拟电动汽车类"""
    def __init__(self, brand, model, year, bettery_size):
        super().__init__(brand, model, year)    # 声明继承父类属性
        """
        self.bettery_size = bettery_size        # 电池容量
        self.electric_quantity = bettery_size   # 电池剩余容量
        self.electric2distance_ratio = 5        # 电量距离转换系数 5 KM / KW·h
        self.remainder_range = self.electric_quantity * self.electric2distance_ratio    # 剩余可行驶里程
        """
        self.bettery = Bettery(bettery_size)
    """
    def get_electric_quantity(self):
        # 查看电车剩余电量
        print("electric quantity: {0}".format(self.bettery.electric_quantity))

    def set_electric_quantity(self, electric_quantity):
        # 考虑输入范围，设置电池剩余电量，重新计算可行驶里程
        if electric_quantity >= 0 and electric_quantity <= self.bettery.bettery_size:
            self.bettery.electric_quantity = electric_quantity
            self.bettery.remainder_range = self.bettery.electric_quantity * self.bettery.electric2distance_ratio
        else:
            print("Wrong Input!")

    def get_remainder_range(self):
        # 查看电车剩余里程距离
        print("remainder_range: {0}".format(self.bettery.remainder_range))

    """
    #  重写父类方法：多态
    def get_main_information(self):
        """获取汽车主要信息"""
        print("brand: {}, model: {}, year: {}, range: {}"
              .format(self.brand, self.model, self.year, self.bettery.bettery_size * self.bettery.electric2distance_ratio))


class Bettery():
    """模拟电动车的电池"""

    def __init__(self, bettery_size=70):
        self.bettery_size = bettery_size
        self.electric_quantity = bettery_size
        self.electric2distance_ratio = 5
        self.remainder_range = self.electric_quantity * self.electric2distance_ratio

    def get_electric_quantity(self):
        print("electric_quantity: {} KW`H".format(self.electric_quantity))

    def set_electric_quantity(self, electric_quantity):
        """设置电池剩余容量，计算电池可支撑里程数"""
        if electric_quantity >= 0 and electric_quantity <= self.bettery_size:
            self.electric_quantity = electric_quantity
            self.remainder_range = self.electric_quantity * self.electric2distance_ratio
        else:
            print("Wrong Input!")

    def get_remainder_range(self):
        """查看剩余里程距离"""
        print("remainder_range: {0}".format(self.remainder_range))

# 创建实例
def main():
    my_new_car = Car("Audi", "A6", 2018)
    print(my_new_car.brand)
    print(my_new_car.model)
    print(my_new_car.year)
    my_new_car.get_main_information()
    temp = my_new_car.get_mileage()
    print(temp)
    # 修改属性
    my_new_car.mileage = 1200
    print(my_new_car.get_mileage())
    # 通过方法调用进行修改
    my_new_car.set_mileage(1400)
    print(my_new_car.get_mileage())
    # 进行属性修改检验
    my_new_car.set_mileage(-80)
    my_new_car.increment_mileage(-80)
    print(my_new_car.get_mileage())

    my_old_car = Car("BMW", "A8", 2017)
    my_cars = [my_new_car, my_old_car]

    my_electric_car = ElectricCar("FF91", "Tomoya", 2048, 1000)
    my_electric_car.get_main_information()
    my_electric_car.bettery.get_electric_quantity()
    my_electric_car.bettery.get_remainder_range()
    my_electric_car.bettery.set_electric_quantity(50)
    my_electric_car.get_main_information()
    my_electric_car.bettery.get_electric_quantity()
    my_electric_car.bettery.get_remainder_range()

    # 重写父类方法
    my_electric_car.get_main_information()


if __name__ == "__main__":
    main()

