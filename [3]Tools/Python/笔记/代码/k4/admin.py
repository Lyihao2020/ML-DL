# admin.py
from user import User

class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print('Admin\'s privileges are following:')
        for privilege in self.privileges:
            print(f'\t{privilege}')

    def add_privilege(self, new_privilege):
        """添加权限"""
        self.privileges.append(new_privilege)

    def remove_privilege(self, privilege_to_remove):
        """删除权限"""
        if privilege_to_remove in self.privileges:
            self.privileges.remove(privilege_to_remove)
        else:
            print(f"{privilege_to_remove} is not in the list of privileges.")

class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()

if __name__ == '__main__':
    new_admin = Admin('Yihao', 'Lai', 21, 'male')

    # 显示用户信息
    new_admin.display_user_info()

    # 显示权限
    new_admin.privileges.show_privileges()

    # 添加新权限
    new_admin.privileges.add_privilege('can edit post')
    new_admin.privileges.show_privileges()

    # 删除权限
    new_admin.privileges.remove_privilege('can delete post')
    new_admin.privileges.show_privileges()



