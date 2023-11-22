# 类的导入
# 在导入过程中要避免命名的冲突

from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model x', 2016)
print(my_tesla.get_descriptive_name())