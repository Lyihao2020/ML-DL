# 传递实参

def describe_pet(animal_type, pet_name='tom'):
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}\'s name is {pet_name.title()}.')

describe_pet('dog', 'Harry')
describe_pet('hamster', 'willie')
describe_pet(pet_name='harry', animal_type='hamster')   # 关键字实参数
describe_pet('cat')





