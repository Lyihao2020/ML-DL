# 继承
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model y', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()