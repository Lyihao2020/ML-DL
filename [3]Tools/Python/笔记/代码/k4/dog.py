class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} is sitting now.')

    def roll_over(self):
        print(f'{self.name.title()} rolled over!')

my_dog = Dog('willie', 6)
print(f'My dog\'s name is {my_dog.name.title()}')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()