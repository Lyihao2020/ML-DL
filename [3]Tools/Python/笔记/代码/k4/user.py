# 练习

class User():
    def __init__(self, first_name, last_name, age, sex):
        """初始化描述用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        """返回整洁的描述信息"""
        full_name = self.first_name + ' ' + self.last_name
        print(f'{full_name.title()} is {self.age} years old.')

    def greet_user(self):
        """向用户发出个性化问候"""
        if self.sex == 'male':
            print(f"Hello, Mr.{self.last_name.title()}.How are you today?")
        else:
            print(f"Hello, Miss.{self.last_name.title()}.How are you today?")

    def increment_login_attempts(self):
        """将登陆尝试次数加一"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登陆尝试次数"""
        self.login_attempts = 0

    def display_user_info(self):
        """显示用户信息"""
        print(f"User Information:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Sex: {self.sex}")

if __name__ == '__main__':
    new_user = User('Yihao', 'Lai', 21, 'male')
    new_user.describe_user()
    new_user.greet_user()

    for i in range(10):
        new_user.increment_login_attempts()
    print(new_user.login_attempts)

    new_user.reset_login_attempts()
    print(new_user.login_attempts)